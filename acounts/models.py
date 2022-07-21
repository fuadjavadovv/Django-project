from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    image = models.ImageField(User,default = "courses/images.jfif",blank=True,null=True)
   


