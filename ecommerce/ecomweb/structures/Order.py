from django.db import models
import datetime
from django.contrib.auth.models import User, auth
from ecomweb.structures.Products import *
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)



    def placeOrder(self):
        self.save()


    @staticmethod
    def get_orders_by_user(username):
        return Order.objects.filter(user=username).order_by('-date')