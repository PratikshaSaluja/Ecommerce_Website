from django.shortcuts import render, redirect
from ecomweb.structures.Products import *
from django.views import View
class cart(View):
    def get(self, request):
        try:
            ids = list(request.session.get('cart').keys())
            print(ids)
            products2 = Product.get_products_by_id(ids)
        except Exception as E:
            print(E)
            return render(request, 'cart/cart.html', {'products2': None})
        return render(request , 'cart/cart.html' ,{'products2':products2})
    def post(self,request):
        try:
            ids = list(request.session.get('cart').keys())
            products2 = Product.get_products_by_id(ids)
            cart = request.session.get('cart')
            for i in products2:
                cart.pop(i.id)
                cart = request.session.update(cart)
                return render(request , 'cart/cart.html' ,{'products2':products2})
        except Exception as E:
            print(E)
            return render(request , 'cart/cart.html' ,{'products2':products2})