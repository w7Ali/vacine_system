from django import forms
from .models import City, Hospital, Patient

input_css = 'form-control'

def add_input_css_class(form):
    """
    Utility function to add the 'form-control' CSS class to all form fields.
    """
    for field_name in form.fields:
        form.fields[field_name].widget.attrs['class'] = input_css

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_input_css_class(self)  # Apply CSS class using the utility function

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_input_css_class(self)  # Apply CSS class using the utility function

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'sex', 'address', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_input_css_class(self)  # Apply CSS class using the utility function