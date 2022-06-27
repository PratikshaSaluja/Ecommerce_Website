from django.shortcuts import render
from ecomweb.structures.Products import *
from ecomweb.structures.cart import *
from django.contrib.auth.decorators import login_required

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        
    return render(request, 'cart/cart.html', {'carts':cart})
              