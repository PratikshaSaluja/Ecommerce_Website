from django.shortcuts import render, redirect
from ecomweb.structures.Products import *
from ecomweb.structures.cart import *
from django.db.models import Q
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
@login_required()
def add_to_cart(request):
    user = request.user
    item_already_in_cart1 = False
    product1 = request.GET.get('product_id')
    item_already_in_cart1 = Cart.objects.filter(Q(product=product1) & Q(user=request.user)).exists()
    if item_already_in_cart1 == False:
    
        product = Product.objects.get(id=product1)
        Cart(user=user,product=product).save()
    return redirect( "/cart")
    