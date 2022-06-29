from django.shortcuts import render, redirect
from django.views import View
from ecomweb.structures.Products import *
from ecomweb.structures.Order import *
from ecomweb.structures.cart import *
class CheckOut(View):
    def post(self, request):
        
            print("gggggggggggggggggggggggggg")
            address_line1 = request.POST.get('address_line1')
            address_line2 = request.POST.get('address_line2')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            phone = request.POST.get('phone')
            
            username1 = request.user.get_username()
            
            user = request.user
            current_user = User.objects.get(username=username1)
            product = Cart.objects.filter(user=user).values('product_id')
       
            print(product)
            print(product[0]["product_id"],15)

            
            print(address_line1,address_line2,state,pincode, phone, username1, product,current_user.id)
          
            order = Order(user_id=current_user.id,
                            
                            address_line1=address_line1,
                            address_line2=address_line2,
                            state=state,
                            pincode=pincode,
                            product_id=product[0]["product_id"],
                            phone=phone,
                            )
            order.save()
            
            return redirect('/order')
        
    def get(self,request):
        try:
            return render(request,'checkout/checkout.html')
        except Exception as E:
            print(E)
            return render(request,'checkout/checkout.html')