from django import forms
from . models import Table1

class Tableform(forms.ModelForm):
    class Meta:
        model=Table1
        fields=['name','email','phone','age','dob']