from django.shortcuts import render, redirect
from ecomweb.structures.Products import *
from django.views import View
class description(View):
    def post(self, request,description_id):
        try:
            desc1 = Product.objects.filter(id=description_id)
            product = request.POST.get('product')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - 1
                    else:
                        cart[product] = quantity + 1

                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1

            request.session['cart'] = cart
            print('cart', request.session['cart'])
            print(desc1)
            return render(request, 'description/description.html',{'desc2' : desc1})
        except Exception as E:
            print(E)
            return render(request, 'description/description.html',{'desc2' : desc1})
    def get(self,request,description_id):
        try:
            desc1 = Product.objects.filter(id=description_id)
            print(desc1)
            return render(request, 'description/description.html',{'desc2' : desc1})
        except Exception as E:
            print(E)
            return render(request, 'description/description.html',{'desc2' : desc1})