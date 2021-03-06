from django.shortcuts import render
from . import forms

# Create your views here.
def user_registration_view(request):
    form = forms.UserRegistrationForm()
    if request.method=='POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print("First Name", form.cleaned_data['first_name'])
            print("Last Name", form.cleaned_data['last_name'])
            print("Email", form.cleaned_data['email'])
    return render(request, 'form_app/user_registration.html', {'form': form})