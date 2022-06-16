from django.shortcuts import render, redirect
from ecomweb.models import service, Product

def sub_category(request,subcategory_id):
    desc = Product.objects.filter(category_id=subcategory_id).values('id','product_name', 'category_id', 'price' ,'desc', 'image')
    return render(request, 'sub_category.html',{'desc':desc})