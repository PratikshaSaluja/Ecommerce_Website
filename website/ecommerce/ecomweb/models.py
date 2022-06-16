from django.db import models
import datetime
from django.contrib.auth.models import User, auth

class service(models.Model):


    serviceheading = models.CharField(max_length=50)

    serviceimage = models.ImageField(upload_to="pics")




class contacts(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    email = models.CharField(max_length=100)
    subject = models.TextField()
    msg = models.TextField()

class categories(models.Model):
    category_id=models.AutoField
    category_name=models.CharField(max_length=200)
    image = models.ImageField(upload_to="pics")

    def __str__(self):
        return self.category_name



class Product(models.Model):

    product_name=models.CharField(max_length=50)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    desc=models.TextField()
    image= models.ImageField(upload_to="pics")

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

class detail(models.Model):
    pdetailid = models.AutoField(primary_key=True)
    pimage = models.ImageField(upload_to="pics")
    
    pcategory = models.CharField(max_length=100)
    pclient = models.CharField(max_length=100)
    pheading = models.CharField(max_length=100)
    pdescription = models.TextField()


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

class author(models.Model):
    authorimage = models.ImageField(upload_to="pics")
    heading = models.CharField(max_length=50)
    subheading = models.CharField(max_length=50)
    description = models.TextField()

