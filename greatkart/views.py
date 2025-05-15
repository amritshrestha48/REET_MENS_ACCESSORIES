from django.shortcuts import render  #import render function from django.shortcuts module
from store.models import Product

def home(request):  #function to handle the home page
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request, 'home.html', context) #render the home.html template

