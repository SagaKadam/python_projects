from django.shortcuts import render

# Create your views here.
def render_template(request):
    my_dict = {"name": "Sagar"}
    return render(request, 'templates_app/first_template.html', context=my_dict)

def render_employee(request):
    my_dict = {"id":111, "name":"Vishal", "salary":10000 }
    return render(request, 'templates_app/employee_template.html', context=my_dict) 
