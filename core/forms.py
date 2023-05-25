from django import forms
from .models import Enrol

class EnrolForm(forms.ModelForm):
    class Meta:
        model = Enrol
        fields = ['name', 'surname', 'email', 'image', 'certificate', 'phone', 'course']
