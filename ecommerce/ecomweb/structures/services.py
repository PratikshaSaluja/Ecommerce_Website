from django.db import models
import datetime
from django.contrib.auth.models import User, auth

class service(models.Model):


    serviceheading = models.CharField(max_length=50)

    serviceimage = models.ImageField(upload_to="pics")