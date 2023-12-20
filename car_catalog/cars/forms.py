

from django import forms
from .models import Car, CarOption

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'price']

class CarPurchaseForm(forms.Form):
    options = forms.ModelMultipleChoiceField(
        queryset=CarOption.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

