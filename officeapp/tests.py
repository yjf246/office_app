from django.test import TestCase
from datetime import datetime

# try:
#     log = Loginornot.objects.get(User=userdetails)
#     if log is not None and log.LogInOrNot == True:
#         return render(request, 'login.html', {'error': "Another session is active. Please log out from the other device before logging in."})
#     if log is not None:
#         log.LogInOrNot = True
#         log.mac_address = macaddress
#         log.save()
# except:
#         log = Loginornot(User = userdetails,LogInOrNot = True,mac_address = macaddress)
#         log.save()