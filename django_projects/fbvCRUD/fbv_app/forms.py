from dataclasses import field
from pyexpat import model
from socket import fromshare
from django import forms
from fbv_app.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields='__all__'