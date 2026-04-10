from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fieldes = '__all__'