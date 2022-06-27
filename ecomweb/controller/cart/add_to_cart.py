from django.shortcuts import render, redirect
from ecomweb.structures.Products import *
from ecomweb.structures.cart import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
@login_required()
def add_to_cart(request):
    user = request.user
    print(user,"}}}}}}}}}}}}}}}}}}}}}}}")
    product1 = request.GET.get('product_id')
    print(product1,":::::::::::::::::::::;;")
    product = Product.objects.get(id=product1)
    Cart(user=user,product=product).save()
    
    return redirect( "/cart")
    