from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pizza, Toppings
from .forms import ToppingsForm, PizzaForm

#Basic home page
def index(request):    
    return render(request, "pizza/index.html", {})
    
#Retrieves topping lists from DB in order by name
def toppings(request):
    topping_list = Toppings.objects.all().order_by('name')
    return render(request, "pizza/toppingslist.html", {'toppings': topping_list})

#Retrieves pizza lists, with toppings, from DB in order by name
def pizzas(request):
    pizza_list = Pizza.objects.all().order_by('name')
    return render(request, "pizza/pizzalist.html", {'pizzas': pizza_list})

#Built funcionality that shows the appropriate form to add items or a "successfully added item" message
#This is also built with add_pizza
def add_toppings(request):
    submitted = False
    if request.method == "POST":
        form = ToppingsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_toppings?submitted=True')
    else:
        form = ToppingsForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "pizza/add_toppings.html", {'form': form, 'submitted': submitted})

#Grabs the primary key id of the selected topping so it can be updated
#Also used on update_pizza
#Used this same structure of using the pk for showing and deleting toppings and pizzas
def update_topping(request, topping_id):
    toppings = Toppings.objects.get(pk=topping_id)
    form = ToppingsForm(request.POST or None, instance=toppings)
    if form.is_valid():
        form.save()
        return redirect("list_toppings")
    return render(request, "pizza/update_topping.html", {'toppings': toppings, 'form': form})


def add_pizza(request):
    submitted = False
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_pizza?submitted=True')
    else:
        form = PizzaForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "pizza/add_pizza.html", {'form': form, 'submitted': submitted})

def show_pizza(request, pizza_id):
    pizza = Pizza.objects.get(pk=pizza_id)
    return render(request, "pizza/show_pizza.html", {'pizza': pizza})

def update_pizza(request, pizza_id):
    pizza = Pizza.objects.get(pk=pizza_id)
    form = PizzaForm(request.POST or None, instance=pizza)
    if form.is_valid():
        form.save()
        return redirect("list_pizzas")
    return render(request, "pizza/update_pizza.html", {'pizza': pizza, 'form': form})

def delete_pizza(request, pizza_id):
    pizza = Pizza.objects.get(pk=pizza_id)
    pizza.delete()
    return redirect('list_pizzas')

def delete_topping(request, topping_id):
    topping = Toppings.objects.get(pk=topping_id)
    topping.delete()
    return redirect('list_toppings')
