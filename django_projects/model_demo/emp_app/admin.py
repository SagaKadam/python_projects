from django.contrib import admin
from emp_app.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'salary', 'email']

admin.site.register(Employee, EmployeeAdmin)