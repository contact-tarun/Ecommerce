from django import forms
from .models import *
class Registration_form_validate(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
    