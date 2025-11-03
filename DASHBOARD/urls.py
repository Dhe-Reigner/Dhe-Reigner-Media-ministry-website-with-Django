from django.urls import path
from .import views

urlpatterns = [
    path('main/',views.main,name='DASHBOARD/main'),
    path('admin/',views.admin,name='DASHBOARD/admin'),
    path('members/',views.members,name='DASHBOARD/members'),
    path('library/',views.library,name='DASHBOARD/library'),
    path('archives/',views.archives,name='DASHBOARD/archives'),
    path('content_calender/',views.content_calender,name='DASHBOARD/content_calender'),
    path('policy_document/',views.policy_document,name='DASHBOARD/policy_document'),
]
