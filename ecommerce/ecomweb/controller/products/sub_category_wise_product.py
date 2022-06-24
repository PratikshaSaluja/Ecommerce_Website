from django.shortcuts import render, redirect
from ecomweb.structures.services import *
from ecomweb.structures.Products import *

def sub_category(request,subcategory_id):
    try:
        desc = Product.objects.filter(category_id=subcategory_id).values('id','product_name', 'category_id', 'price' ,'desc', 'image')
        return render(request, 'sub_category/sub_category.html',{'desc':desc})
    except Exception as E:
        print(E)
        return render(request, 'sub_category/sub_category.html',{'desc':desc})
