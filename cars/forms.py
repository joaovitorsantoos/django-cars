from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')

        if factory_year < 1975:
            self.add_error('factory_year', 'Insira um carro fabricado depois de 1975.')
        return factory_year

    def clean_value(self):
        value = self.cleaned_data.get('value')

        if value < 15000:
            self.add_error('value', 'Insira um carro com valor minimo de R$ 15.000')
        return value