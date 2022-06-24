from django.shortcuts import render, redirect
from ecomweb.structures.Order import *
from django.contrib.auth.models import User, auth
from django.views import View
class OrderView(View):
    def get(self , request ):
        try:
            user1 = request.session.get('username')
            user = User.objects.get(username=user1)
            print(user1)
            orders = Order.get_orders_by_user(user.id)
            print(orders)
            return render(request, 'orders/order.html', {'orders': orders})
        except Exception as E:
            print(E)
            return render(request, 'orders/order.html', {'orders': orders})