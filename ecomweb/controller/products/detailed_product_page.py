from django.shortcuts import render, redirect
from ecomweb.structures.Products import *
from ecomweb.structures.cart import *
from django.views import View
from django.db.models import Q
class description(View):
    def get(self,request,description_id):
        try:
            desc1 = Product.objects.filter(id=description_id)
           
            
            print(desc1)
            return render(request, 'description/description.html',{'desc2' : desc1 })
        except Exception as E:
            print(E)
            return render(request, 'description/description.html',{'desc2' : desc1})