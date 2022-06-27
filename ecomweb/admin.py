from django.contrib import admin
from ecomweb.structures.Order import *
from ecomweb.structures.services import *
from ecomweb.structures.Products import *
from ecomweb.structures.categories import *
from ecomweb.structures.Order import *
from ecomweb.structures.detail import *
from ecomweb.structures.author import *
from ecomweb.structures.contact import *
from ecomweb.structures.banner import *
from ecomweb.structures.cart import *
admin.site.register(categories)
admin.site.register(service)
admin.site.register(contacts)
admin.site.register(Product)
admin.site.register(detail)
admin.site.register(Order)
admin.site.register(author)
admin.site.register(banner)
admin.site.register(Cart)





