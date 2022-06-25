from django.db import models
import datetime
from django.contrib.auth.models import User, auth
class author(models.Model):
    authorimage = models.ImageField(upload_to="pics")
    heading = models.CharField(max_length=50)
    subheading = models.CharField(max_length=50)
    description = models.TextField()