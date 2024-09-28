from django.db import models
import datetime
from datetime import date




# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class UserProfile(models.Model):
    UserId = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=50, blank=False, null=False)
    MiddleName = models.CharField(max_length=50, blank=False, null=False)
    LastName = models.CharField(max_length=50, blank=False, null=False)
    BirthDate = models.DateField(blank=True, null=True)
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    PresentAddress = models.TextField(blank=True, null=True)
    PermanentAddress = models.TextField(blank=True, null=True)
    City = models.CharField(max_length=100,blank=True, null=True)
    State = models.CharField(max_length=100,blank=True, null=True)
    PinCode = models.IntegerField(blank=True, null=True)
    Mobile = models.IntegerField(blank=True, null=True)
    # EmergencyPhoneNo = models.IntegerField(blank=True, null=True)
    BloodGroup = models.CharField(max_length=10,blank=True, null=True)
    Email = models.EmailField(unique=True,blank=True, null=True)
    JoiningDate = models.DateField(blank=True, null=True)
    Qualification = models.CharField(max_length=100,blank=True, null=True)
    # RefName = models.CharField(max_length=50,blank=True, null=True)
    # RefMo = models.IntegerField(blank=True, null=True)
    UserName = models.CharField(max_length=50, blank=False, null=False,unique=True)
    Password = models.CharField(max_length=50, blank=False, null=False)
    UploadDocument = models.FileField(upload_to='user_documents/%d_%m_%Y/', blank=True, null=True)
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    mac_address = models.CharField(max_length=17, blank=True, null=True)

    def __str__(self):
        return str(self.UserName)


TASK_STATUS = (
    ('PENDING', 'PENDING'),
    ('COMPLETED', 'COMPLETED'),
)

class Task(models.Model):
    Markasdone = models.CharField(max_length=100,default='PENDING',choices=TASK_STATUS)
    TaskName = models.CharField(max_length=255)
    Addedby = models.CharField(max_length=50, blank=False, null=False)
    # AasignedTo = models.TextField(blank=True, null=True)
    TaskAddedTime = models.DateField(default=str(date.today()))
    DueDate = models.DateField(blank=True, null=True)
    Category = models.TextField(blank=True, null=True)
    ProjectAbout = models.TextField(blank=True, null=True)
    Keyword1 = models.TextField(blank=True, null=True)
    Keyword2 = models.TextField(blank=True, null=True)
    Keyword3 = models.TextField(blank=True, null=True)
    Remarks = models.TextField(blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Attachments = models.FileField(upload_to='Attachments/',blank=True, null=True)
    def __str__(self):
        return self.TaskName
    
PROJECT_NAME = (
    ('scdp1','scdp1'),
    ('scdp2','scdp2'),
    ('mealplan','mealplan'),
    ('other','other')
)
TASK_TYPE = (
    ('service','service'),
    ('development','development'),
    ('incident','incident'),
    ('other','other')
)
TASK_SUBTYPE = (
    ('software','software'),
    ('hardware','hardware'),
    ('other','other')
)
TASK_PRIORITY = (
    ('low','low'),
    ('medium','medium'),
    ('high','high')
)

class TaskActions(models.Model):
    TaskAddBy = models.CharField(max_length=50,default='')
    TaskTitle = models.CharField(max_length=255)
    ProjectName = models.CharField(max_length=100,blank=True, null=True,choices=PROJECT_NAME)
    TaskType = models.CharField(max_length=100,blank=True, null=True,choices=TASK_TYPE)
    TaskSubtype = models.CharField(max_length=100,blank=True, null=True,choices=TASK_SUBTYPE)
    TaskPriority = models.CharField(max_length=100,blank=True, null=True,choices=TASK_PRIORITY)
    TaskStart = models.DateTimeField(blank=True, null=True)
    TaskClosed = models.DateTimeField(blank=True, null=True)
    TaskSLA = models.IntegerField(blank=True, null=True ,default=1)
    RootCase = models.CharField(max_length=1000,blank=True, null=True)
    Correction = models.CharField(max_length = 1000,blank=True, null=True,default=" ")
    CorrectiveAction = models.CharField(max_length = 1000,blank=True, null=True,default=" ")
    Description = models.CharField(max_length = 1000,blank=True, null=True,default=" ")
    Attachments = models.FileField(upload_to='Attachments/',blank=True, null=True)
    Markasdone = models.CharField(max_length=100,default='PENDING',choices=TASK_STATUS)
    def __str__(self):
        return self.TaskTitle


class CheckIO(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    defaultdate = models.DateTimeField(default=str(datetime.datetime.now()))
    duration = models.CharField(max_length=100, blank=True, null=True)
    

class Policy(models.Model):
    Policyname = models.CharField(max_length=255)
    Attachments = models.FileField(upload_to='CompanyPolicy/',blank=True, null=True)
    def __str__(self):
        return self.Policyname

class Event(models.Model):
    eventname = models.CharField(max_length=255)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()

LEAVE_CHOICES = (
    ('Sick Leave', 'Sick Leave'),
    ('Casual Leave', 'Casual Leave'),
    ('Personal Leave', 'Personal Leave'),
    ('Emergency Leave', 'Emergency Leave'),
)

LEAVE_STATUS = (
    ('PENDING', 'PENDING'),
    ('REJECTED', 'REJECTED'),
    ('APPROVED', 'APPROVED'),
)

class Leave(models.Model):
    leavestatus = models.CharField(max_length = 100, default='PENDING',choices=LEAVE_STATUS) 
    leaveid = models.AutoField(primary_key=True)
    requestby = models.CharField(max_length=255)
    startdate = models.DateField(default=str(date.today()))
    enddate = models.DateField()
    # days = models.IntegerField()
    leavetype = models.CharField(max_length=255,choices=LEAVE_CHOICES)
    reason = models.TextField()
    Remarks = models.TextField(default=" ")
    def __str__(self):
        return self.requestby

# class Chetbox(models.Model):
#     Chetid = models.AutoField(primary_key=True)
#     Userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
#     Message = models.CharField(max_length=1000)
#     Attachments = models.FileField(upload_to='Attachments/',blank=True, null=True)

class Holiday(models.Model):
    HolidayName = models.CharField(max_length=255)
    HolidayDate = models.DateField()
    
class Announcements(models.Model):
    Announcement = models.CharField(max_length = 1000)
    date = models.DateField(default=str(date.today()))

class Activeusers(models.Model):
    User = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Active = models.BooleanField(default=False)
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    Ip_address = models.CharField(max_length=20, blank=True, null=True)
    Domain_name = models.CharField(max_length=50, blank=True, null=True)
    

