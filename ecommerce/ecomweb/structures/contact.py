from django.db import models
import datetime
from django.contrib.auth.models import User, auth
class contacts(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    email = models.CharField(max_length=100)
    subject = models.TextField()
    msg = models.TextField()