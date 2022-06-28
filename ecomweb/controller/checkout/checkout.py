from django.shortcuts import render, redirect
from django.views import View
from ecomweb.structures.Products import *
from ecomweb.structures.Order import *
class CheckOut(View):
    def post(self, request):
        try:
            address_line1 = request.POST.get('address_line1')
            address_line2 = request.POST.get('address_line2')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            phone = request.POST.get('phone')
            username1 = request.session.get('username')
            cart = request.session.get('cart')
            products = Product.get_products_by_id(list(cart.keys()))
            current_user = User.objects.get(username=username1)
            print(address_line1,address_line2,state,pincode, phone, username1, cart, products,current_user.id)
            for product in products:
                print(cart.get(str(product.id)))
                order = Order(user_id=current_user.id,
                            product=product,
                            price=product.price,
                            address_line1=address_line1,
                            address_line2=address_line2,
                            state=state,
                            pincode=pincode,
                            phone=phone,
                            )
                order.save()
            
            return redirect('/order')
        except Exception as E:
            print(E)
            return render(request,'checkout/checkout.html')
    def get(self,request):
        try:
            return render(request,'checkout/checkout.html')
        except Exception as E:
            print(E)
            return render(request,'checkout/checkout.html')