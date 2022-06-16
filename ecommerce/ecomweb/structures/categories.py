from django.db import models
import datetime
from django.contrib.auth.models import User, auth
class categories(models.Model):
    category_id=models.AutoField
    category_name=models.CharField(max_length=200)
    image = models.ImageField(upload_to="pics")

    def __str__(self):
        return self.category_name