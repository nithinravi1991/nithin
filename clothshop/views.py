from django.shortcuts import render
from django.http import HttpResponse
from.models import Product
# Create your views here.
def index(request):
    clothshop=Product.objects.all()
    return render(request,'fort.html',{'clothshop':clothshop})
    #return HttpResponse("<h1>Welcome to ClothShop</h1>")
def about(request):
    return HttpResponse("<h1>About ClothShop</h1>")