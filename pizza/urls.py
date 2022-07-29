from django.urls import path
from . import views


urlpatterns = [    
    path('', views.index, name="index"),
    path("pizzas/", views.pizzas, name="list_pizzas"),
    path('owners/', views.toppings, name="list_toppings"),    
    path('add_toppings/', views.add_toppings, name='add_toppings'),
    path('update_topping/<topping_id>', views.update_topping, name="update_topping"),
    path('add_pizza/', views.add_pizza, name='add_pizza'),
    path('show_pizza/<pizza_id>', views.show_pizza, name='show_pizza'),
    path('update_pizza/<pizza_id>', views.update_pizza, name='update_pizza'),
    path('delete_pizza/<pizza_id>', views.delete_pizza, name='delete_pizza'),
    path('delete_topping/<topping_id>', views.delete_topping, name='delete_topping'),
]