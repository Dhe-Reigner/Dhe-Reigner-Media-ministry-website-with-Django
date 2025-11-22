from django.shortcuts import render,get_object_or_404
from . models import Employee,Farm

# Create your views here.
def index(request):
    employees = Employee.objects.all()
    return render(request,'DASHBOARD/index.html',{
        'employees':employees
    })

def employee_dashboard(request):
    return render(request,'EMPLOYEES/employee-dashboard.html')

def employee(request):
    employees = Employee.objects.all()
    return render(request,'EMPLOYEES/employee.html',{
        'employees':employees
    })

def employee_details(request,id_number):
    details =  get_object_or_404(Employee,id_number=id_number)
    return render(request,'EMPLOYEES/employee-details.html',{
        'details':details
    })

def add_employee(request):
    return render(request,'EMPLOYEES/add-employee.html')

def edit_employee(request):
    return render(request,'EMPLOYEES/edit-employee.html')

def departments(request):
    return render(request,'DEPARTMENTS/departments.html')

def farms(request):
    farms = Farm.objects.all()
    return render(request,'FARMS/farms.html',{
        'farms':farms
    })

def farm_details(request):
    return render(request,'FARMS/farm-details.html')