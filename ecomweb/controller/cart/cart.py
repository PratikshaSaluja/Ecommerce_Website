# from django.shortcuts import render, redirect
# from ecomweb.structures.Products import *
# from ecomweb.structures.cart import *
# from django.views import View
# from django.contrib import messages
# class cart(View):
#     # def get(self, request):
#     # #     user = request.user
    
#     # #     product_id = request.GET.get('id')
#     # #     product = Product.objects.get(id=product_id)
#     # #     Cart(user=user,product=product).save()
#     # #     print(product_id,":::::::::::::::::::::;;")
#     # # #     try:
#     # #         ids = list(request.session.get('cart').keys())
#     # #         print(ids)
#     # #         products2 = Product.get_products_by_id(ids)
#     # #     except Exception as E:
#     # #         print(E)
#     # #         return render(request, 'cart/cart.html', {'products2': None})
#     #     # return render(request , 'cart/cart.html' ,{'products2':products2})
#     #     return render(request , 'cart/cart.html' )
#     def post(self,request):
#         try:
#             ids = list(request.session.get('cart').keys())
#             products2 = Product.get_products_by_id(ids)
#             cart = request.session.get('cart')
#             for i in products2:
#                 cart.pop(i.product_id)
#                 cart = request.session.update(cart)
#                 return render(request , 'cart/cart.html' ,{'products2':products2})
#         except Exception as E:
#             print(E)
#             return render(request , 'cart/cart.html' ,{'products2':products2})