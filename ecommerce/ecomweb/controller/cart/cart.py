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
            ids = list(request.session.get('cart').keys())
            ids1 = list(request.session.get('cart'))
            print(ids1,"^^^^^^^^^^^^^^^^^^^^^^^^^^")
            products2 = Product.get_products_by_id(ids)
            print(products2,"************************")
            cart = request.session.get('cart')
            
            print(cart,"________________________")
            #del request.session['cart']
            for i in products2:
                cart.pop(i.id)
                cart = request.session.update(cart)
            
            
            print(cart,"(((((((((((((((((((((")

            return render(request , 'cart/cart.html' ,{'products2':products2})