from django.shortcuts import render,get_object_or_404
from . models import Employee,Farm
from .forms import EmployeeForm

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
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            new_id_number = form.cleaned_data['id_number']
            new_employee_image = form.cleaned_data['employee_image']
            new_name = form.cleaned_data['name']
            new_id_image = form.cleaned_data['id_image']
            new_gender = form.cleaned_data['gender']
            new_date = form.cleaned_data['date']
            new_mobile_number = form.cleaned_data['mobile_number']
            new_assignment = form.cleaned_data['assignment']

            new_employee = Employee(
                id_number = new_id_number,
                employee_image = new_employee_image,
                name = new_name,
                id_image =new_id_image,
                gender = new_gender,
                date = new_date,
                mobile_number = new_mobile_number,
                assignment = new_assignment
            )
            new_employee.save()
            return render(request,'EMPLOYEES/employee.html',{
                'form':EmployeeForm(),
                'success':True
            })
    else:
        form = EmployeeForm()
        return render(request,'EMPLOYEES/add-employee.html',{
            'form':EmployeeForm()
        })

def edit_employee(request):
    return render(request,'EMPLOYEES/edit-employee.html')

def departments(request):
    return render(request,'DEPARTMENTS/departments.html')

def farms(request):
    farms = Farm.objects.all()
    return render(request,'FARMS/farms.html',{
        'farms':farms
    })

def farm_details(request,farm_number):
    farm_details = get_object_or_404(Farm,farm_number=farm_number)
    return render(request,'FARMS/farm-details.html',{
        'farm_details':farm_details
    })

def edit_farm(request):
    return render(request,'FARMs/edit-farm.html')