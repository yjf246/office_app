from django.urls import path 
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('base/',views.base,name='base'),
    path('signin/',views.signin,name='signin'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('manageadmin/',views.manageadmin,name='manageadmin'),
    path('editadmin/<int:UserId>',views.editadmin,name='editadmin'),
    path('usermanagement/',views.usermanagement,name='usermanagement'),
    path('edituser/<int:UserId>',views.editUser, name="editUser"),
    path('deleteuser/<int:UserId>',views.usermanagement, name="deleteuser"),
    path('editISuser/<int:UserId>',views.editIsUser, name="editIsUser"),
    path('showuser/<int:UserId>',views.showuser, name="showuser"),
    path('usertask/',views.usertask, name="usertask"),
    path('markdone/<int:id>',views.markdone, name="markdone"),
    path('updatetaskremark/<int:id>',views.updatetaskremark, name="updatetaskremark"),
    path('taskdelete/<int:id>',views.taskdelete, name="taskdelete"),
    path('calender/',views.calender, name="calender"),
    path('policy/',views.policy, name="policy"),
    path('checkinout/',views.checkinout, name="checkinout"),
    path('leave/',views.mangeLeave, name="leave"),
    path('updateleaveremark/<int:leaveid>',views.updateLeaveremark, name="updateleaveremark"),
    path('statusleave/<int:leaveid>',views.statusleave, name="statusleave"),
    path('holidayspage/',views.holidayfun, name="holidayspage"),
    path('deleteholiday/<int:id>',views.holidayfun, name="deleteholiday"),
    path('birthdays/',views.birthdayfun, name="birthdays"),
    path('activeusers/',views.Activeuser, name="activeusers"),
    path('hiren/',views.Activeuser, name="activeusers"),
    path('TaskDetails/',views.taskDetails, name="TaskDetails"),
    path('upTaActn/<int:id>',views.updateTaskAction, name="upTaActn"),
    path('mkdNTskAtn/<int:id>',views.markdoneTaskAction, name="mkdNTskAtn"),
    path('TaskReport/',views.taskReport, name="TaskReport"),

]

UserMenulist = [
    # ['User Task','/usertask','bi bi-journal-text'],
    ['Task Details','/TaskDetails','bi bi-journal-text'],
    ['Task Report','/TaskReport','ri-file-copy-2-line'],
    ['Event Calendar','/calender','bi bi-calendar'],
    ['Company Policy','/policy','ri-menu-fill'],
    ['Check-In Check-Out','/checkinout','ri-login-box-fill'],
    ['Leave Details','/leave','ri-logout-circle-r-line'],
    ['Holiday List','/holidayspage','ri-gallery-line'],
    ['Birthdays','/birthdays','ri-cake-2-fill'],
    
    ]

AminMenulist = [
    # ['User Task','/usertask','bi bi-journal-text'],
    ['Task Details','/TaskDetails','bi bi-journal-text'],
    ['Task Report','/TaskReport','ri-file-copy-2-line'],
    ['Active Users','/activeusers','ri-ghost-2-line'],
    ['Admin Page','/manageadmin','ri-contacts-fill'],
    ['User Management','/usermanagement','ri-group-fill'],
    ['Event Calendar','/calender','bi bi-calendar'],
    ['Check-In Check-Out','/checkinout','ri-login-box-fill'],
    ['Company Policy','/policy','ri-menu-fill'],
    ['Leave Details','/leave','ri-logout-circle-r-line'],
    ['Holiday List','/holidayspage','ri-gallery-line'],
    ['Birthdays','/birthdays','ri-cake-2-fill'],
    
    ]
