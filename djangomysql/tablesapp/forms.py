# tablesapp/forms.py

from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'course', 'semester', 'contact_number', 'email_id', 'address']
