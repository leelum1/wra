from django import forms
from licensing_app.models import Abstraction_Point

class AbstractionLicense(forms.ModelForm):
    class Meta:
        model = Abstraction_Point
        fields = ['source_type','abstraction_period']
