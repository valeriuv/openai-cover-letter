from django import forms
from crispy_forms.helper import FormHelper

class InputForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control', 'id': 'floatingInput'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control', 'id': 'floatingInput'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control', 'id': 'floatingInput'}))
    position = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Position', 'class': 'form-control', 'id': 'floatingInput'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()