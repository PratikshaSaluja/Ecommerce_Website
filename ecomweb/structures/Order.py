from django.db import models
import datetime
from django.contrib.auth.models import User, auth
from ecomweb.structures.Products import *
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    address_line1 = models.CharField(max_length=50, default='', blank=True)
    address_line2 = models.CharField(max_length=50, default='', blank=True)
    state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    state = models.CharField(choices=state_choices,max_length=255, null=True, blank=True)
    pincode = models.IntegerField(default="000000")
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)



    def placeOrder(self):
        self.save()


    @staticmethod
    def get_orders_by_user(username):
        return Order.objects.filter(user=username).order_by('-date')