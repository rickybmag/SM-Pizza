from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pizza.urls")),
    path('toppings/', include("pizza.urls")),
    path('pizzas/', include("pizza.urls")),
]
