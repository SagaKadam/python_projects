from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    GENDER = [('male', 'MALE'), ('fenale', 'FEMALE')]
    first_name= forms.CharField(required=False, validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(10)])
    last_name= forms.CharField()
    email= forms.CharField()
    gender= forms.CharField(widget=forms.Select(choices=GENDER))
    password= forms.CharField(widget=forms.PasswordInput)
    ssn = forms.IntegerField()

    def clean_first_name(self):
        input_first_name = self.cleaned_data['first_name']
        if(len(input_first_name) > 20):
            raise forms.ValidationError('The max length of firstname is 20')
        return input_first_name

    def clean_email(self):
        input_email = self.cleaned_data['email']
        if input_email.find('@')==-1:
            raise forms.ValidationError('The email should contain @')