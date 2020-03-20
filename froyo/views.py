from django.shortcuts import render

# Create your views here.

def froyo(request):
    return render(request, 'froyo.html')

def ingredients(request):
    return render(request, 'ingredients.html')

def ingredients_list(request):
    return render(request, 'ingredients_list.html')

def ingredients_detail(request):
    return render(request, 'ingredients_detail.html')

def ingredients_update(request):
    return render(request, 'ingredients_update_form.html')

def ingredients_create(request):
    return render(request, 'ingredients_create_form.html')


def recipes(request):
    return render(request, 'recipes.html')

def recipes_list(request):
    return render(request, 'recipes_list.html')

def recipes_detail(request):
    return render(request, 'recipes_detail.html')

def recipes_update(request):
    return render(request, 'recipes_update_form.html')

def recipes_create(request):
    return render(request, 'recipes_create_form.html')


def orders(request):
    return render(request, 'orders.html')

def orders_list(request):
    return render(request, 'orders_list.html')

def orders_detail(request):
    return render(request, 'orders_detail.html')

def orders_update(request):
    return render(request, 'orders_update_form.html')

def orders_create(request):
    return render(request, 'orders_create_form.html')
