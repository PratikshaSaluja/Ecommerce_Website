from django.shortcuts import render, redirect
from ecomweb.structures.Order import *
from ecomweb.structures.services import *
from ecomweb.structures.Products import *
from ecomweb.structures.categories import *
from ecomweb.structures.Order import *
from ecomweb.structures.author import *
from ecomweb.structures.banner import *
from django.views import View

class Home(View):


    def get(self,request):
        service1 = service.objects.all()
        author1 = author.objects.all()
        banner1 = banner.objects.values('image')
        allProds = categories.objects.values('id','image','category_name')
        return render(request, "home/home2.html", {'allProds': allProds, 'serv100': service1 , 'author1':author1,'banner2':banner1})