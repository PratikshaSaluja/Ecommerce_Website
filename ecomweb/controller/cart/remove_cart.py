from django.shortcuts import render, redirect, HttpResponse
from ecomweb.structures.Products import *
from ecomweb.structures.cart import *
from django.db.models import Q
from django.http import JsonResponse
from django.db.models import Q

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['product_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0

        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)

            amount += tempamount

        data = {
            'amount':amount,
            'totalamount':amount
        }
        return JsonResponse(data)
    else:
        return HttpResponse("")