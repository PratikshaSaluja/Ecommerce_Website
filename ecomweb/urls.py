from django.urls import path
from django.contrib.auth.decorators import login_required
from ecomweb.controller.authentication.signin import *
from ecomweb.controller.registration.signup import *
from ecomweb.controller.products.category_wise_product import *
from ecomweb.controller.products.sub_category_wise_product import *
from ecomweb.controller.products.detailed_product_page import *
from ecomweb.controller.cart.showcart import *
from ecomweb.controller.cart.cart_quantity import *
from ecomweb.controller.cart.add_to_cart import *
from ecomweb.controller.cart.remove_cart import *
from ecomweb.controller.services.services import *
from ecomweb.controller.contact.contact import *
from ecomweb.controller.checkout.checkout import *
from ecomweb.controller.order.order import *
from ecomweb.controller.portfolio.portfolio import *


urlpatterns = [

    path('', Home.as_view(), name="Home"),
    path('login',login, name='login'),
    path('logout', logout, name='logout'),
    path('signup', signup, name='signup'),
    path('services',services, name='services'),
    path('portfolio/<str:productdetail_id>/', portfolio, name='portfolio'),
    path('description/<str:description_id>/', description.as_view(), name='description'),
    path('contact', contact.as_view(), name='contact'),
    path('cart', show_cart , name='showcart'),
    path('pluscart', plus_cart , name='plus_cart'),
    path('minuscart', minus_cart , name='minus_cart'),
    path('removecart', remove_cart , name='remove_cart'),
    path('add_to_cart', add_to_cart , name='add_to_cart'),
    path('sub_category/<str:subcategory_id>/', sub_category, name='sub_category'),
    path('checkout', CheckOut.as_view() , name='checkout'),
    path('order', login_required(OrderView.as_view()) , name='order'),



    ]