from django.contrib import admin
from . models import Employee


# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    list_display = ('id_number','employee_image','name','id_image','gender','date','mobile_number')
admin.site.register(Employee,employeeAdmin)
