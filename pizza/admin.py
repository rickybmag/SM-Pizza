from django.contrib import admin
from .models import Pizza
from .models import Toppings

@admin.register(Toppings)
class ToppingsAdmin(admin.ModelAdmin):    
    ordering = ('name',)

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):    
    ordering = ('name',)