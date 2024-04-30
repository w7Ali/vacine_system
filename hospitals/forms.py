from django import forms
from .models import City, Hospital

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'