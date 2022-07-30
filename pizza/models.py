from django.db import models


class Toppings(models.Model):    
    name = models.CharField(null=True, max_length=25, unique=True)    

    def __str__(self):
        return self.name

#Toppings is a M2M relationship because pizza can have multiple toppings
class Pizza(models.Model):
    name = models.CharField("Pizza", null=True, blank=True, unique=True, max_length=25)
    toppings = models.ManyToManyField(Toppings)

    def __str__(self):
        return self.name

