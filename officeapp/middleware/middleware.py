# middleware.py

from datetime import datetime, timedelta
from django.utils import timezone
from officeapp.models import UserProfile, CheckIO

class UpdateCheckInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.last_update_time = timezone.now()

    def __call__(self, request):
        response = self.get_response(request)
        
        if timezone.now() - self.last_update_time >= timedelta(minutes=0):
            self.update_check_ins(request)
            self.last_update_time = timezone.now()
        
        return response
    
    def update_check_ins(self, request):
        if 'loguser' in request.session and 'check_in' in request.session:
            loguser = request.session['loguser']
            userdetails = UserProfile.objects.get(UserName=loguser)
            check_in = request.session['check_in']

            x_datetime = datetime.strptime(check_in, '%Y-%m-%d %H:%M:%S.%f')
            y_datetime = datetime.now()
            duration = y_datetime - x_datetime
            obj = CheckIO.objects.get(check_in=check_in, user_profile=userdetails)
            
            obj.duration = str(duration)
            obj.save()
