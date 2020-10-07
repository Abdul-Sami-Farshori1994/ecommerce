from django.shortcuts import render
from .models import product
from math import ceil
from django.http import HttpResponse

# Create your views here.
def index(request):
    products = product.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nslides,'range': range(1,nslides),'product':products}
    return render(request,'shop/index.html',params)
def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    return HttpResponse("we are at contact")
def tracker(request):
    return HttpResponse("we are at tracker")
def search(request):
    return HttpResponse("we are at search")
def productview(request):
    return HttpResponse("we are at productview")
def checkout(request):
    return HttpResponse("we are at checkout")
