from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='DASHBOARD/index'),
    path('employee-dashboard/',views.employee_dashboard,name='DASHBOARD/employee-dashboard'),
    path('employee/',views.employee,name='DASHBOARD/employee'),
    path('add-employee/',views.add_employee,name='DASHBOARD/add-employee'),
    path('edit-employee/',views.edit_employee,name='DASHBOARD/edit-employee'),
    path('employee-details/<str:id>',views.employee_details,name='DASHBOARD/employee-details'),
]
