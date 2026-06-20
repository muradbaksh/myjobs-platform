from django import forms
from .models import Compensation

class CompensationForm(forms.ModelForm):
    class Meta:
        model = Compensation
        # exclude = ['user']
        exclude = ['user', 'company']