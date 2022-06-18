from django import forms
from .models import *

class Coop12Form(forms.ModelForm):
    class Meta:
        model = Coop12
        fields = '__all__'