from django.shortcuts import render
from . models import Employee

# Create your views here.
def index(request):
    return render(request,'DASHBOARD/index.html')

def employee_dashboard(request):
    return render(request,'DASHBOARD/employee-dashboard.html')

def employee(request):
    employees = Employee.objects.all()
    return render(request,'DASHBOARD/employee.html',{
        'employees':employees
    })

def employee_details(request,id):
    details =  Employee.objects.all(id=id)
    return render(request,'DASHBOARD/employee-details.html',{
        'details':details
    })

def add_employee(request):
    return render(request,'DASHBOARD/add-employee.html')

def edit_employee(request):
    return render(request,'DASHBOARD/edit-employee.html')