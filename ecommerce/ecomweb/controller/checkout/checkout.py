from django.shortcuts import render, redirect
from django.views import View
class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        username1 = request.session.get('username')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        current_user = User.objects.get(username=username1)
        print(address, phone, username1, cart, products,current_user.id)
        for product in products:
            print(cart.get(str(product.id)))
            order = Order(user_id=current_user.id,
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          )
            order.save()
        request.session['cart'] = {}
        return redirect('order')
    def get(self,request):
        return render(request,'checkout.html')