from django.urls import path
from ecomweb.controller.authentication.signin import *
from ecomweb.controller.registration.signup import *
from ecomweb.controller.products.category_wise_product import *
from ecomweb.controller.products.sub_category_wise_product import *
from ecomweb.controller.products.detailed_product_page import *
from ecomweb.controller.cart.cart import *
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
    path('contact', contact, name='contact'),
    path('cart', cart, name='cart'),

    path('sub_category/<str:subcategory_id>/', sub_category, name='sub_category'),
    path('checkout', CheckOut.as_view() , name='checkout'),
    path('order', OrderView.as_view() , name='order'),



    ]