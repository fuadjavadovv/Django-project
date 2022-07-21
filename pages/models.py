from django.db import models
from django.urls.conf import path

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank = True)

    def __str__(self):
        return self.email
