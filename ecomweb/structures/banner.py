from django.db import models
import datetime
from django.contrib.auth.models import User, auth
class banner(models.Model):
    image = models.ImageField(upload_to="pics")