from django.shortcuts import render
from ecomweb.structures.Products import *
from ecomweb.structures.cart import *
from django.contrib.auth.decorators import login_required

@login_required
def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount=0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.price)
                amount += tempamount
               
        
            return render(request, 'cart/cart.html', {'carts':cart, 'amount':amount,'totalitem':totalitem})
        else:
            return render(request, 'cart/emptycart.html', {'totalitem':totalitem})
    else:
        return render(request, 'cart/emptycart.html', {'totalitem':totalitem})
              

