from statistics import mode
from django.shortcuts import render
from emp_app.models import Employee

# Create your views here.
def employee_data(request):
    employees = Employee.objects.all()
    empl_dict = {'employees': employees}
    return render(request, 'employees.html', context=empl_dict)
