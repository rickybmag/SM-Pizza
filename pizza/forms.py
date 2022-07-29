from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Toppings, Pizza

#Creates Toppings Form
class ToppingsForm(ModelForm):
    class Meta:
        model = Toppings
        fields = "__all__"
        labels = {
            'name': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Add your own toppings to Pizzaria SM's Menu"})
        }

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza        
        fields = "__all__"
        labels = {            
            'name': 'Pizza',     
            'topping': 'Best',       
        }
        widgets = {
            'pizza': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Pizza Name"})
        }