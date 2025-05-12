from django.shortcuts import render  #import render function from django.shortcuts module

def home(request):  #function to handle the home page
    return render(request, 'home.html') #render the home.html template