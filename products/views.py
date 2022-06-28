from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
    #return HttpResponse("Hello, world. You're at the products index.")
def about(request):
    return HttpResponse("Hello, world. You're at the products about.")

# Create your views here.
