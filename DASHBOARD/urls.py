from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='DASHBOARD/index'),
    path('employee-dashboard/',views.employee_dashboard,name='EMPLOYEES/employee-dashboard'),
    path('employee/',views.employee,name='EMPLOYEES/employee'),
    path('add-employee/',views.add_employee,name='EMPLOYEES/add-employee'),
    path('edit-employee/',views.edit_employee,name='EMPLOYEES/edit-employee'),
    path('employee-details/<int:id_number>',views.employee_details,name='EMPLOYEES/employee-details'),
    path('departments/',views.departments,name='DEPARTMENTS/departments'),
    path('farms/',views.farms,name='FARMS/farms'),
    path('farm-details/<int:farm_number>',views.farm_details,name='FARMS/farm-details'),
]
