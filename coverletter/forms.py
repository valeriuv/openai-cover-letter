from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Application
from accounts.models import CustomUser
from crispy_forms.helper import FormHelper

class InputForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control', 'id': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control', 'id': 'last_name'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control', 'id': 'company'}))
    position = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Position', 'class': 'form-control', 'id': 'position'}))
    job_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Copy and paste the job description here...', 'class': 'form-control', 'id': 'description', 'style': 'height: 100px'}))
    cv = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file' ,'id': 'cv'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

class ApplicationForm(forms.ModelForm):
    #user = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User', 'class': 'form-control', 'id': 'user'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Application name', 'class': 'form-control', 'id': 'name'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control', 'id': 'company'}))
    job_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Position', 'class': 'form-control', 'id': 'job_title'}))
    job_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Copy and paste the job description here...', 'class': 'form-control', 'id': 'description', 'style': 'height: 100px'}))
    cv = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file' ,'id': 'cv'}))
    
    class Meta:
        model = Application
        fields = ['user', 'name', 'company', 'job_title', 'job_description', 'cv']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]