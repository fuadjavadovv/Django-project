from django.db import models
from django.db.models.fields import CharField
from teachers.models import Teacher
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,null=True)
    slug = models.SlugField(max_length=200, unique=True,null=True)


    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    slug = models.SlugField(max_length=200, unique=True,null=True)


    def __str__(self):
        return str(self.name)
class Course(models.Model):
    teacher = models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE, related_name="courses")
    name = models.CharField(max_length=200,unique=True)
    category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    tag= models.ManyToManyField(Tag,blank=True,null=True)
    students = models.ManyToManyField(User,blank=True,related_name='courses_joined')
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/",default = "courses/images.jfif")
    date = models.DateTimeField(auto_now=True)
    avilable = models.BooleanField(default=True)
    # hit = models.PositiveIntegerField(default=True)

    def __str__(self):
        return str(self.name)


class Comment(models.Model):
    course = models.ForeignKey(Course,on_delete = models.CASCADE,verbose_name = "Makaale", related_name="comments")
    comment_user = models.CharField(max_length = 50,verbose_name = "Isim")
    comment_description = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return str(self.course.name)
    