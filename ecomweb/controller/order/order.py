from django.shortcuts import render, redirect
from ecomweb.structures.Order import *
from django.contrib.auth.models import User, auth
from django.views import View
class OrderView(View):
    def get(self , request ):
        try:
            user= request.user
            orders = Order.objects.filter(user=user).all()
            print(orders)
            return render(request, 'orders/order.html', {'orders': orders})
        except Exception as E:
            print(E)
            return render(request, 'orders/order.html')