from django.shortcuts import render, redirect
from ecomweb.structures.Order import *
from ecomweb.structures.services import *
from ecomweb.structures.Products import *
from ecomweb.structures.categories import *
from ecomweb.structures.Order import *
from ecomweb.structures.author import *
from ecomweb.structures.banner import *
from django.views import View
from django.db.models import Q

class Home(View):
    def get(self,request):
        try:
            search= request.GET.get('search','')
            service1 = service.objects.all()
            author1 = author.objects.all()
            banner1 = banner.objects.values('image')
            allProds = categories.objects.filter(category_name__icontains=search).values('id','image','category_name')
            return render(request, "home/home2.html", {'allProds': allProds, 'serv100': service1 , 'author1':author1,'banner2':banner1,'search':search})
        except Exception as E:
            print(E)
            return render(request, "home/home2.html", {'allProds': allProds, 'serv100': service1 , 'author1':author1,'banner2':banner1,'search':search})
    def post(self,request):
        try:
            search = request.POST.get('search')
            desc = Product.objects.filter(Q(product_name__icontains=search)| Q(category_id__category_name=search)).values('id','product_name', 'category_id', 'price' ,'desc', 'image')
            if desc :
                return render(request, 'sub_category/sub_category.html', {'search':search,'desc':desc})
            else:
                return render(request, 'sub_category/emptysearch.html')
        except Exception as E:
            print(E)
            return render(request, 'sub_category/emptysearch.html', {'search':search,'desc':desc})