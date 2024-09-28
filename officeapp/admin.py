from django.contrib import admin
from .models import UserProfile,Task,CheckIO,Policy,Event,Leave,Holiday,Announcements,Activeusers,TaskActions

# Register your models here.
@admin.register(UserProfile)
class UserModel(admin.ModelAdmin):
    list_display = ['UserName','Password','UserId','is_user','is_admin']

@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ['id','TaskName','TaskAddedTime']

@admin.register(TaskActions)
class TaskActions(admin.ModelAdmin):
    list_display = ['id','TaskTitle','TaskStart']

@admin.register(Activeusers)
class ActiveusersAdmin(admin.ModelAdmin):
    list_display = ['User','Active','mac_address']

@admin.register(CheckIO)
class CheckIO(admin.ModelAdmin):
    list_display = ['id','user_profile','check_in','check_out','duration','defaultdate']

@admin.register(Policy)
class CheckIO(admin.ModelAdmin):
    list_display = ['Policyname','Attachments']

@admin.register(Event)
class CheckIO(admin.ModelAdmin):
    list_display = ['eventname','starttime','endtime']

@admin.register(Leave)
class CheckIO(admin.ModelAdmin):
    list_display = ['leaveid','requestby','startdate','leavetype']

@admin.register(Holiday)
class Holidayadmin(admin.ModelAdmin):
    list_display = ['HolidayName','HolidayDate']

@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['Announcement']

