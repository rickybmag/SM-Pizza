from django.db import models

#Creates a pizza and topping model that have a one to one relationship. Toppings needs to connect with pizza so pizza has more than one item
class Toppings(models.Model):    
    name = models.CharField(null=True, max_length=25, unique=True)    

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField("Pizza", null=True, blank=True, unique=True, max_length=25)
    toppings = models.ManyToManyField(Toppings)

    def __str__(self):
        return self.name

