from django.db import models
import datetime
from ecomweb.structures.Products import *
from django.contrib.auth.models import User, auth
class Cart(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)
 def __str__(self):
  return str(self.id)
  
 
 @property
 def total_cost(self):
   return self.quantity * self.product.discounted_price
