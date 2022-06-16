from django.shortcuts import render, redirect
from ecomweb.structures.Products import *
def description(request , description_id):
    desc1 = Product.objects.filter(id=description_id).values('id','product_name', 'quantity', 'category_id', 'price' ,'desc', 'image')
    return render(request, 'description.html',{'desc2' : desc1})