from django.shortcuts import render,redirect
from .models import UserProfile,Task,CheckIO,Policy,Event,Leave,Holiday,Announcements,Activeusers,TaskActions
from django.conf import settings
from django.core.cache import cache
from . import urls 
from django.contrib import messages
from django.utils import timezone
import json
from json import JSONEncoder
import datetime
from datetime import date
from django.db.models.functions import ExtractMonth,ExtractDay
from django.http import JsonResponse
from .utils import get_client_ip_and_mac,get_domain_name

# views.py
def Session_require(view_func):
    def wrapped_view(request, *args, **kwargs):
        try:
            if request.session.test_cookie_worked():
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/login/')
        except:
            return redirect('/login/')
    return wrapped_view

def Check_UrlInMenu(view_func):
    def check_Url(request, *args, **kwargs):
        if not request.get_full_path()[:-1] in [i[1] for i in request.session['menubar']] :
            return redirect('/login/')
        else:
            return view_func(request, *args, **kwargs)
    return check_Url

def Admin_only(view_func):
    def wrapped_view(request, *args, **kwargs):
        try:
            if request.session['is_admin'] is True:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/login/')
        except:
            return redirect('/login/')
    return wrapped_view

def isUser(view_func):
    def wrapped_view(request, *args, **kwargs):
        try:
            if request.session['is_user'] is True:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/login/')
        except:
            return redirect('/login/')
    return wrapped_view

def base(request):
    return render(request,'base.html')

@isUser
@Session_require
def index(request):
    context = {}

    if request.method=="POST":
        anounce = request.POST['announcements'] 
        newanounce = Announcements(Announcement=anounce)
        newanounce.save()
        return redirect('/index/')

    if request.session.test_cookie_worked():
        loguser = request.session['loguser']
        leaves = Leave.objects.all().order_by('-leaveid')
        pendingleave = [i for i in leaves if (loguser == str(i.requestby) and i.leavestatus == 'PENDING') or (request.session['is_admin'] is True and i.leavestatus == 'PENDING')]
        context['pendingleave'] = pendingleave

        user = UserProfile.objects.all()
        context['users'] = user
        today = str(date.today())

        bdt = [i.UserName for i in user if str(i.BirthDate).split("-")[1:] == str(today).split("-")[1:]]
        context['bdt'] = bdt

        events = Event.objects.all()
        event = [i.eventname for i in events if str(i.starttime).split(' ')[0]==today]
        context['event'] = event

        announcements = Announcements.objects.all()
        announcement = [i.Announcement for i in announcements if str(i.date) == today]
        context['announcement'] = announcement

        tasks = Task.objects.all()
        pendingtask = [i for i in tasks if (loguser == (str(i.Addedby)) and i.Markasdone == 'PENDING') or (request.session['is_admin'] is True and i.Markasdone == 'PENDING')]
        context['pendingtask'] = pendingtask

        checkinout = CheckIO.objects.all().order_by('-id')[:8]
        newcheckinout = [i for i in checkinout if loguser == (str(i.user_profile)) or request.session['is_admin'] is True]
        context['checks'] = newcheckinout 

        return render(request,'index.html',context)
    else:
        return redirect('/login/')

def signin(request):
    cache.clear()
    request.session.clear()
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    if request.method == 'POST':
        FirstName = request.POST['firstname']
        MiddleName = request.POST['middlename']
        LastName = request.POST['lastname']
        BirthDate = request.POST['birthdate']
        Gender = request.POST['gender']
        PresentAddress = request.POST['presentaddress']
        PermanentAddress = request.POST['permanentaddress']
        City = request.POST['city']
        State = request.POST['state']
        PinCode = request.POST['pincode']
        Mobile = request.POST['mobile']
        BloodGroup = request.POST['bloodgroup']
        Email = request.POST['email']
        JoiningDate = request.POST['joindate']
        Qualification = request.POST['qualification']
        UserName = request.POST['username']
        Password = request.POST['password']
        UploadDocument = request.FILES['doc']

        new_user = UserProfile(FirstName= FirstName,MiddleName=MiddleName,LastName=LastName,
                                        BirthDate=BirthDate,Gender=Gender,PresentAddress=PresentAddress,
                                        PermanentAddress=PermanentAddress,City=City,State=State,
                                        PinCode=PinCode,Mobile=Mobile,
                                        BloodGroup=BloodGroup,Email=Email,
                                        JoiningDate=JoiningDate,Qualification=Qualification,
                                        UserName=UserName,Password=Password,UploadDocument=UploadDocument)
        new_user.save()
        messages.success(request, 'User signed up successfully. You can now log in.')
        return redirect("/login/")

    return render(request,'signin.html')

def login(request):
    if request.session.test_cookie_worked():
        loguser = request.session['loguser']
        userdetails = UserProfile.objects.get(UserName=loguser)
        check_in = request.session['check_in'].replace("+00:00", "") 
        check_out = str(datetime.datetime.now())
        x_datetime = datetime.datetime.strptime(check_in, '%Y-%m-%d %H:%M:%S.%f')
        y_datetime = datetime.datetime.strptime(check_out, '%Y-%m-%d %H:%M:%S.%f')
        duration = y_datetime - x_datetime
        obj = CheckIO.objects.get(check_in=check_in,user_profile=userdetails)
        obj.check_out = check_out
        obj.duration = str(duration)
        obj.save()
    
        cache.clear()
        request.session.clear()
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
    else:
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()

    if request.method == 'POST':
        UserName = request.POST['username']
        Password = request.POST['password']
        
        try:
            userdetails = UserProfile.objects.get(UserName=UserName,Password=Password) 
            ip_address, mac_address1 = get_client_ip_and_mac(request)
            domain_name = get_domain_name(ip_address)
            try:
                alllog = Activeusers.objects.all()
                activelog =  [i.mac_address for i in alllog if i.Active == True]
                log = Activeusers.objects.get(User=userdetails)
                # if log is not None and log.Active == True and log.mac_address != mac_address1:
                #     return render(request, 'login.html', {'error': "Another session is active. Please log out from the other device before logging in."})
                # elif  log is not None and log.Active == False and (mac_address1 in activelog):
                #     return render(request, 'login.html', {'error': "Another session is active. Please log out before logging in."})
                     
                if log is not None:
                    log.Active = True
                    log.mac_address = mac_address1
                    log.Ip_address = ip_address
                    log.Domain_name = domain_name
                    log.save()
            except:
                log = Activeusers(User = userdetails,Active = True,mac_address = mac_address1,Ip_address= ip_address,Domain_name = domain_name)
                log.save()
            
            request.session['mac_address'] = (ip_address,mac_address1,domain_name)
            request.session['is_user'] = userdetails.is_user
            request.session['is_admin'] = userdetails.is_admin
            request.session['logid'] = userdetails.UserId
            request.session['logfirstname'] = userdetails.FirstName
            request.session['loglastname'] = userdetails.LastName
            request.session['loguser'] = userdetails.UserName
            request.session['logprofile'] = str(userdetails.UploadDocument.url)
            request.session['check_in'] = str(datetime.datetime.now())
            request.session['defaultdate'] = str(datetime.datetime.now())
            request.session['logout_before_close'] = False
            
            request.session['menubar'] = urls.AminMenulist if userdetails.is_admin == True else urls.UserMenulist

            request.session.save()
            request.session.set_test_cookie()

            checkin = CheckIO(user_profile=userdetails, check_in=request.session['check_in'])
            checkin.save()
            return redirect('/index/')
        except:
            return render(request,'login.html', {'error': "Invalid Username or Password"})
    return render(request,'login.html')

@Session_require
def logout(request):
    loguser = request.session['loguser']
    userdetails = UserProfile.objects.get(UserName=loguser)
    check_in = request.session['check_in']
    check_out = str(datetime.datetime.now())
    x_datetime = datetime.datetime.strptime(check_in, '%Y-%m-%d %H:%M:%S.%f')
    y_datetime = datetime.datetime.strptime(check_out, '%Y-%m-%d %H:%M:%S.%f')

    duration = y_datetime - x_datetime

    obj = CheckIO.objects.get(check_in=check_in,user_profile=userdetails)
    obj.check_out = check_out
    obj.duration = str(duration)
    obj.save()

    log = Activeusers.objects.get(User=userdetails)
    log.Active = False
    log.save()

    cache.clear()
    request.session.clear()
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    return redirect('/login/')

@Session_require    
@Check_UrlInMenu
def manageadmin(request):
    context  = {}
    demps = UserProfile.objects.all()
    context['demps'] = demps
    return render(request,'manageadmin1.html',context)

@Session_require
@Admin_only
def editadmin(request,UserId):
    if request.method == 'POST':
        is_admin = request.POST['isadmin']
        updatequery = UserProfile.objects.get(UserId=UserId)
        updatequery.is_admin = is_admin
        updatequery.save()
        return redirect("/manageadmin/")

@Session_require
@Admin_only
def editIsUser(request,UserId):
    if request.method == 'POST':
        is_user = request.POST['isuser']
        updatequery = UserProfile.objects.get(UserId=UserId)
        updatequery.is_user = is_user
        updatequery.save()
        return redirect("/manageadmin/")

@Admin_only
@Session_require
@Check_UrlInMenu
def usermanagement(request,UserId=0):
    context = {}    
    users = UserProfile.objects.all()
    context['users'] = users
    if request.method == 'POST':
        FirstName = request.POST['first_name']
        MiddleName = request.POST['middle_name']
        LastName = request.POST['last_name']
        BirthDate = request.POST['birthdate']
        Gender = request.POST['gender']
        PresentAddress = request.POST['presentaddress']
        PermanentAddress = request.POST['permanentaddress']
        City = request.POST['city']
        State = request.POST['state']
        PinCode = request.POST['pincode']
        Mobile = request.POST['mobile_number']
        BloodGroup = request.POST['bloodgroup']
        Email = request.POST['email']
        JoiningDate = request.POST['joiningdate']
        Qualification = request.POST['qualification']
        UserName = request.POST['username']
        Password = request.POST['password']
        UploadDocument = request.FILES.get('profilepicture')

        new_reg_emp = UserProfile(FirstName= FirstName,MiddleName=MiddleName,LastName=LastName,
                                        BirthDate=BirthDate,Gender=Gender,PresentAddress=PresentAddress,
                                        PermanentAddress=PermanentAddress,City=City,State=State,
                                        PinCode=PinCode,Mobile=Mobile,BloodGroup=BloodGroup,Email=Email,
                                        JoiningDate=JoiningDate,Qualification=Qualification,UserName=UserName,
                                        Password=Password,UploadDocument=UploadDocument)
        new_reg_emp.save()

        return redirect("/usermanagement/")

    if UserId:
        try:
            User_to_be_removed = UserProfile.objects.get(UserId=UserId)
            User_to_be_removed.delete()
            return redirect("/usermanagement/")
        except:
            return redirect("/usermanagement/")
    return render(request,'usermanagement1.html',context)

@isUser
@Session_require
def editUser(request,UserId):
    fetchuserdetails= UserProfile.objects.get(UserId=UserId)
    context={
        "Userdetails":fetchuserdetails        
    }
    if (request.session['logid']== UserId or request.session['is_admin'] is True):
        if request.method == 'POST':
            FirstName = request.POST['first_name']
            MiddleName = request.POST['middle_name']
            LastName = request.POST['last_name']
            BirthDate = request.POST['birthdate']
            Gender = request.POST['gender']
            PresentAddress = request.POST['presentaddress']
            PermanentAddress = request.POST['permanentaddress']
            City = request.POST['city']
            State = request.POST['state']
            PinCode = request.POST['pincode']
            Mobile = request.POST['mobile_number']
            BloodGroup = request.POST['bloodgroup']
            Email = request.POST['email']
            JoiningDate = request.POST['joiningdate']
            Qualification = request.POST['qualification']
            # UserName = request.POST['username']
            Password = request.POST['password']
            UploadDocument = request.FILES.get('profilepicture')

            updatequery = UserProfile.objects.get(UserId=UserId)
            updatequery.FirstName = FirstName
            updatequery.MiddleName = MiddleName
            updatequery.LastName = LastName
            updatequery.BirthDate = BirthDate
            updatequery.Gender = Gender
            updatequery.PresentAddress = PresentAddress
            updatequery.PermanentAddress = PermanentAddress
            updatequery.City = City
            updatequery.State = State
            updatequery.PinCode = PinCode
            updatequery.Mobile = Mobile
            updatequery.BloodGroup = BloodGroup
            updatequery.Email = Email
            updatequery.JoiningDate = JoiningDate
            updatequery.Qualification = Qualification
            # updatequery.UserName = UserName
            updatequery.Password = Password
            
            if UploadDocument is not None:
                updatequery.UploadDocument = UploadDocument

            updatequery.save()
            if request.session['is_admin'] is True:
                return redirect("/usermanagement/")
            else:
                return redirect('/index/')
        
        return render(request,'edituser.html',context)
    else:
        return redirect('/login/')

@isUser
@Session_require
def showuser(request,UserId):
    context = {}
    fetchuserdetails= UserProfile.objects.get(UserId=UserId)
    context["Userdetails"]=fetchuserdetails        
    return render(request,'showuser.html',context)

@isUser
@Session_require
@Check_UrlInMenu
def usertask(request):

    context = {}
    users = UserProfile.objects.all()
    context['users'] = users

    if request.method=="POST":
        taskname = request.POST['taskname']
        addedby = request.POST['addedby']
        duedates = request.POST['duedate']
        category = request.POST['category']
        ProjectAbout = request.POST['projectabout']
        Keyword1 = request.POST['keyword1']
        Keyword2 = request.POST['keyword2']
        Keyword3 = request.POST['keyword3']
        Remark = request.POST['Remark1']
        description = request.POST['description']
        attachments = request.FILES.get('attachments')

        newtask = Task(TaskName=taskname,Addedby=addedby,DueDate=duedates,Remarks=Remark,
                       ProjectAbout = ProjectAbout,Keyword1=Keyword1,Keyword2=Keyword2,Keyword3=Keyword3,
                       Category=category,Description=description,Attachments=attachments)
        newtask.save()
        return redirect('/usertask/')
    
    alltasks = Task.objects.all().order_by('-id')
    loguser = request.session['loguser']
    alltasks = [i for i in alltasks if loguser == (str(i.Addedby)) or request.session['is_admin'] is True]
    context["alltasks"]=alltasks   
    return render(request,'usertask.html',context)

@isUser
@Session_require
@Check_UrlInMenu
def taskDetails(request):

    context = {}
    users = UserProfile.objects.all()
    context['users'] = users

    if request.method=="POST":
        taskAddBy = request.POST['taskaddby']
        taskTitle = request.POST['tasktitle']
        projectName = request.POST['projectname']
        taskType = request.POST['tasktype']
        taskSubtype = request.POST['tasksubtype']
        taskPriority = request.POST['taskpriority']
        taskStart = request.POST['taskstart']
        taskClosed = request.POST['taskclosed']
        taskSLA = request.POST['taskSla']
        rootCase = request.POST['rootcase']
        correction_ = request.POST['correction']
        corrective_action = request.POST['correctiveaction']
        description_ = request.POST['description']

        attachments = request.FILES.get('Attachments')

        newtask = TaskActions(TaskAddBy=taskAddBy,TaskTitle=taskTitle,ProjectName=projectName,TaskType=taskType,TaskSubtype=taskSubtype,
                       TaskPriority = taskPriority,TaskStart=taskStart,TaskClosed=taskClosed,TaskSLA=taskSLA,RootCase=rootCase,Correction=correction_,
                       CorrectiveAction=corrective_action,Description=description_,Attachments=attachments)
        newtask.save()
        return redirect('/TaskDetails/')
    
    alltasks = TaskActions.objects.all().order_by('-id')
    loguser = request.session['loguser']
    alltasks = [i for i in alltasks if loguser == (str(i.TaskAddBy)) or request.session['is_admin'] is True]
    context["alltasks"]=alltasks   
    return render(request,'TaskDetails.html',context)

@isUser
@Session_require
def updateTaskAction(request,id):
    if request.method=="POST":

        task_Title = request.POST['taskTitle']
        project_Name = request.POST['projectName']
        task_Type = request.POST['taskType']
        task_Subtype = request.POST['taskSubtype']
        task_priority = request.POST['taskpriority']
        root_case = request.POST['rootCase']
        correction_ = request.POST['_correction']
        correctiveAction_ = request.POST['_correctiveAction']
        description_ = request.POST['_description']
        
        updatequery = TaskActions.objects.get(id=id)
        updatequery.TaskTitle = task_Title
        updatequery.ProjectName = project_Name
        updatequery.TaskType = task_Type
        updatequery.TaskSubtype = task_Subtype
        updatequery.TaskPriority = task_priority
        updatequery.RootCase = root_case
        updatequery.Correction = correction_
        updatequery.CorrectiveAction = correctiveAction_
        updatequery.Description = description_
        updatequery.save()
        return redirect('/TaskDetails/') 
    
@isUser
@Session_require
def markdoneTaskAction(request,id):
    if request.method=='POST':
        Markasdone = request.POST['mkdN_TskAtn']
        updatequery = TaskActions.objects.get(id=id)
        updatequery.Markasdone = Markasdone
        updatequery.save()
    return redirect('/TaskDetails/')

@isUser
@Session_require
def updatetaskremark(request,id):
    if request.method=="POST":
        newremarks = request.POST['remarks']
        newdescription = request.POST['description']
        newkeyword1 = request.POST['keyword1']
        newkeyword2 = request.POST['keyword2']
        newkeyword3 = request.POST['keyword3']

        updatequery = Task.objects.get(id=id)
        updatequery.Remarks = newremarks
        updatequery.Description = newdescription
        updatequery.Keyword1 = newkeyword1
        updatequery.Keyword2 = newkeyword2
        updatequery.Keyword3 = newkeyword3
        updatequery.save()
        return redirect('/usertask/') 

@isUser
@Session_require
def markdone(request,id):
    if request.method=='POST':
        Markasdone = request.POST['markdone']
        updatequery = Task.objects.get(id=id)
        updatequery.Markasdone = Markasdone
        updatequery.save()
    return redirect('/usertask/')

@isUser
@Session_require
def taskdelete(request,id):
    deletequery = Task.objects.get(id=id)
    deletequery.delete()
    return redirect('/usertask/')

@isUser
@Check_UrlInMenu
@Session_require
def calender(request):
    context = {}
    users = UserProfile.objects.all()
    context['users'] = users
    lst = [
        ['3','my schedule 3 ','2024-01-26 09:41:35.392491','2024-01-27 18:06:05.392491'],
        ['4','my schedule 4','2024-01-28 09:41:35.392491','2024-01-29 18:06:05.392491']]
    context['lst'] = lst
    if request.method=="POST":
        eventname = request.POST['eventname']
        starttime = (request.POST['startdatetime']).replace("T"," ").replace("Z","")
        endtime = (request.POST['enddate']).replace("T"," ").replace("Z","")
        newevent = Event(eventname=str(eventname),starttime=starttime,endtime=endtime)
        newevent.save()
        return redirect('/calender/')
    events = Event.objects.all()
    context['events'] = events
    return render(request,'calender.html',context)

@isUser
@Session_require
@Check_UrlInMenu
def policy(request):
    context = {}
    users = UserProfile.objects.all()
    context['users'] = users

    if request.method=="POST":
        policyname = request.POST['policyname']
        attachments = request.FILES.get('attachments')

        newpolicy = Policy(Policyname=policyname,Attachments=attachments)
        newpolicy.save()
        return redirect('/policy/')
    allpolicy = Policy.objects.all().order_by('-id')
    context["allpolicy"] = allpolicy 

    return render(request,'policy.html',context=context)

def total_time(durations):
    total_seconds = 0
    for duration in durations:
        hours, minutes, seconds = map(float, duration.split(':'))
        total_seconds += hours * 3600 + minutes * 60 + seconds
    total_hours = total_seconds // 3600
    total_seconds %= 3600
    total_minutes = total_seconds // 60
    total_seconds %= 60
    return total_hours, total_minutes, total_seconds

@isUser
@Session_require
@Check_UrlInMenu
def checkinout(request):
    context = {}
    
    if request.session['is_admin'] is False:
        user = UserProfile.objects.get(UserName=request.session['loguser'])
        context['users'] = user
    else:
        users = UserProfile.objects.all()
        context['users'] = users

    if request.method=="POST":
        userprofile = request.POST.get('userprofile')
        if request.session['is_admin'] is True or request.session['loguser']==userprofile:
            u = UserProfile.objects.get(UserName=userprofile)
        else:
            return redirect('/checkinout/')
        user = [u.FirstName,u.LastName]
        starttime = (request.POST['startdatetime']).replace("T"," ").replace("Z","")
        endtime = (request.POST['enddatetime']).replace("T"," ").replace("Z","")
        check = CheckIO.objects.all().order_by('-id')
        x = [i for i in check if ((starttime=='' and endtime == '') or starttime < str(i.defaultdate) < endtime) and userprofile == (str(i.user_profile))]
        durations = [i.duration for i in x if i.duration is not None]
        total_hours, total_minutes, total_seconds = total_time(durations)
        total_duration = f'Total time: {int(total_hours)} hours, {int(total_minutes)} minutes, and {total_seconds:.2f} seconds'

        context['userprofile'] = user
        context['starttime'] = starttime
        context['endtime'] = endtime
        context['x'] = x
        context['y'] = total_duration
    return render(request,'checkinout.html',context)

@isUser
@Session_require
@Check_UrlInMenu
def taskReport(request):
    context = {}
    table_head = ["Task AddBy","Task Title","Project Name","Task Type","Task Subtype","Task Priority","Task Start","Task Closed","Task SLA","Root Case","Mark as Done"]
    context['table_head'] = table_head


    # if request.method=="POST":

    #     starttime = (request.POST['startdatetime']).replace("T"," ").replace("Z","")
    #     endtime = (request.POST['enddatetime']).replace("T"," ").replace("Z","")
    check = TaskActions.objects.all().order_by('-id')

    # context['starttime'] = starttime
    # context['endtime'] = endtime
    context['x'] = check
    return render(request,'TaskReport.html',context)

@isUser
@Session_require
@Check_UrlInMenu
def mangeLeave(request):
    context = {}
    users = UserProfile.objects.all()
    context['users'] = users
    leaves = Leave.objects.all().order_by('-leaveid')
    loguser = request.session['loguser']
    leave = [i for i in leaves if loguser == (str(i.requestby)) or request.session['is_admin'] is True]
    context['leaves'] = leave

    if request.method=="POST":
        requestby = request.POST['requestby']
        startdate = request.POST['Startdate']
        enddate = request.POST['Enddate']
        leavetype = request.POST['leavetype']
        reason = request.POST['Reason']

        newrequest = Leave(requestby=requestby,startdate=startdate,enddate=enddate,leavetype=leavetype,reason=reason)
        newrequest.save()
        return redirect('/leave/')
    return render(request,'leave.html',context)

@Admin_only
@Session_require
def statusleave(request,leaveid):
    if request.method=="POST":
        status = request.POST['status']
        updatestatus = Leave.objects.get(leaveid=leaveid)
        updatestatus.leavestatus = status
        updatestatus.save()
        return redirect("/leave/")
    
@isUser
@Session_require
def updateLeaveremark(request,leaveid):
    if request.method=="POST":
        newremarks = request.POST['remarks']
        updatequery = Leave.objects.get(leaveid=leaveid)
        updatequery.Remarks = newremarks
        updatequery.save()
        return redirect('/leave/') 

@isUser
@Session_require
def holidayfun(request,id=0):
    context = {}
    holidays_ = Holiday.objects.all().values().order_by('HolidayDate')
    context['holidays'] = holidays_
    if request.method == "POST":
        holidayname = request.POST['holiday']
        holidaydate = request.POST['holidaydate']
        _holiday = Holiday(HolidayName=holidayname,HolidayDate=holidaydate)
        _holiday.save()
        return redirect('/holidayspage/')
    if id:
        try:
            deletequery = Holiday.objects.get(id=id)
            deletequery.delete()
            return redirect("/holidayspage/")
        except:
            return redirect("/holidayspage/")
    return render(request,'holidays.html',context)

@isUser
@Session_require
@Check_UrlInMenu
def birthdayfun(request):
    context = {}
    users = UserProfile.objects.annotate(month=ExtractMonth('BirthDate'),day=ExtractDay('BirthDate')).order_by('month','day')
    bdays = [[i.FirstName,i.LastName,i.BirthDate] for i in users]
    context['bdays'] = bdays
    return render(request,'birthday.html',context)

@isUser
@Session_require
def Activeuser(request):
    context = {}
    loguser = Activeusers.objects.all()
    context['loguser'] = loguser
    return render(request,'activeusers.html',context)