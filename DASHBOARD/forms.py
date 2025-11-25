from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =  ('id_number','employee_image','name','id_image','gender','date','mobile_number','assignment')
        labels = {
            'id_number':'id_number',
            'employee_image':'',
            'name':'name',
            'id_image':'',
            'gender':'gender',
            'date':'date',
            'mobile_number':'mobile_number',
            'assignment':'assignment'
        }
        widgets = {
            'id_number':forms.NumberInput(attrs={'class':'form-control'}),
            'employee_image':forms.FileInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'id_image':forms.FileInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control'}),
            'mobile_number':forms.NumberInput(attrs={'class':'form-control'}),
            'assignment':forms.TextInput(attrs={'class':'form-control'})
        }