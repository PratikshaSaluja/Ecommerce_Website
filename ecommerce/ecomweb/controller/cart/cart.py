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
            products2 = Product.get_products_by_id(ids)
            cart = request.session.get('cart')
            
            product = Product.objects.get(id=request.GET.get('id'))
            print(product,"+++++++++++++++++++")
            print(cart,"******************")
            print(ids,"_______")
            print(request.GET.get('id'))
            print(product.id,type(product.id))
            print(ids)
            id = str(product.id)
            print(type(id))
            ids.remove(id)
    
            return render(request , 'cart/cart.html' ,{'products2':products2})