from django.shortcuts import render
from .models import product
from math import ceil
from django.http import HttpResponse

# Create your views here.
def index(request):
   # products = product.objects.all()
   # print(products)
    #n = len(products)
   # nslides = n//4 + ceil((n/4)-(n//4))

    allprods= []
    catprods= product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides])

   # params = {'no_of_slides':nslides,'range': range(1,nslides),'product':products}
   #allprods = [[products, range(1, nslides), nslides],
                #[products, range(1, nslides), nslides]]
    params = {'allprods': allprods}
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
