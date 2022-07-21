from django.contrib import admin
from .models import Category, Course,Tag,Comment

# Register your models here.
admin.site.register(Comment)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name","avilable",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}    




