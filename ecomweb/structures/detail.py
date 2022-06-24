from django.db import models
import datetime
from django.contrib.auth.models import User, auth
class detail(models.Model):
    pdetailid = models.AutoField(primary_key=True)
    pimage = models.ImageField(upload_to="pics")
    
    pcategory = models.CharField(max_length=100)
    pclient = models.CharField(max_length=100)
    pheading = models.CharField(max_length=100)
    pdescription = models.TextField()