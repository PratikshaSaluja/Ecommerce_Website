from django.shortcuts import render, redirect
from ecomweb.structures.Products import *
from django.views import View
class description(View):
    def post(self, request):
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
        return redirect('/description')
    def get(self,request,description_id):
        desc1 = Product.objects.filter(id=description_id).values('id','product_name', 'quantity', 'category_id', 'price' ,'desc', 'image')
        return render(request, 'description/description.html',{'desc2' : desc1})