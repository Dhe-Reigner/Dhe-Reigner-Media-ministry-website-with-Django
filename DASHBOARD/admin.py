from django.contrib import admin
from . models import Employee,Farm


# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    list_display = ('id_number','employee_image','name','id_image','gender','date','mobile_number')
admin.site.register(Employee,employeeAdmin)


class farmAdmin(admin.ModelAdmin):
    list_display = ('farm_number','farm_image','name','description')
admin.site.register(Farm,farmAdmin)