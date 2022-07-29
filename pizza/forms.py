from django import forms
from django.forms import ModelForm
from .models import Toppings, Pizza
from logging import PlaceHolder

#Creates Toppings Form
class ToppingsForm(ModelForm):
    class Meta:
        model = Toppings
        fields = "__all__"
        labels = {
            'name': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza        
        fields = "__all__"        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Pizza Name",}),
            'toppings':forms.SelectMultiple(attrs={'class':'form-control'})            
        }