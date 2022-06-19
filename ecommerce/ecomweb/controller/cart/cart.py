from django.shortcuts import render, redirect
from ecomweb.structures.Products import *
def cart( request):
    try:
         ids = list(request.session.get('cart').keys())
         products2 = Product.get_products_by_id['ids']
    except Exception as E:
        print(E)
        return render(request, 'cart/cart.html', {'products2': None})
    return render(request , 'cart/cart.html' ,{'products2':products2})