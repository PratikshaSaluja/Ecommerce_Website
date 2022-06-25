from django.db import models
import datetime
from django.contrib.auth.models import User, auth
from ecomweb.structures.categories import *
class Product(models.Model):

    product_name=models.CharField(max_length=50)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    desc=models.TextField()
    image= models.ImageField(upload_to="pics")

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)