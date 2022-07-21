
from typing import final, get_args
from django.http import request
from django.shortcuts import redirect, render,get_object_or_404,reverse
from .models import Category,Tag, Course,Comment
from django.conf.urls import url
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import F

# Create your views here.
# def course_list(request):
#     courses = Course.objects.all().order_by('-date')
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

    

def course_list(request, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None
    categories = categories = Category.objects.all()
    tags = Tag.objects.all()
    courses = Course.objects.all().order_by('-date')
    paginator = Course(courses, 2) # Show 25 contacts per page.
    current_user =  request.user


    if category_slug != None:
        messages.add_message(request, messages.ERROR, 'Belə bir kurs tapılmadı')
        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter( avilable=True, category= category_page)

    elif tag_slug != None:
        tag_page = get_object_or_404(Tag, slug=tag_slug)
        courses = Course.objects.filter( avilable=True, tags=tag_page)

    else:
       if current_user.is_authenticated:
            enrolled_courses = current_user.courses_joined.all()
            courses = Course.objects.all().order_by('-date')
            for course in enrolled_courses:
                courses = courses.exclude(id = course.id)
              
       else:
            courses = Course.objects.all().order_by('-date')
            
      


    context = {
        'courses': courses,
        'categories': categories,
        'tags':tags,
    
        "paginator" : paginator

    }

    return render(request, 'courses.html', context)


    
# def category_list(request, category_slug):

#     courses = Course.objects.all().filter(category__slug = category_slug)
#     categories = Category.objects.all()
#     context = {
#         'courses': courses,
#         "categories" : categories,
#         }

#     return render(request, 'courses.html', context)    



# def tag_list(request, tag_slug):

#     courses = Course.objects.all().filter(tag__slug = tag_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     context = {
#         'courses': courses,
#         "categories" : categories,
#         "tags" : tags
#         }

#     return render(request, 'courses.html', context) 

def course_detail(request, category_slug, course_id):
    current_user = request.user
    course = Course.objects.get(category__slug=category_slug, id = course_id)
    courses = Course.objects.all().order_by('-date') 
    categories = categories = Category.objects.all()
    
    comments = course.comments.all()
    # commentsall = course.comments.all()
    # post_comment = course.comments.all().count()

      
    tags = Tag.objects.all()
    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()

    else:
        enrolled_courses = courses

    #enrolled_courses = current_user.courses_joined.all()
   
    context = {
        'course': course,
        'enrolled_courses': enrolled_courses,
        'categories': categories,
        'tags': tags,
        "comments":comments,
      
      

        
  
    }
   
       
    return render(request, 'course.html', context)




def search(request):
  courses = Course.objects.filter(name__contains = request.GET['search'])
  messages.add_message(request, messages.ERROR, 'Belə bir kurs tapılmadı')
  categories = Category.objects.all()
  tags = Tag.objects.all()
  context = {
         'courses': courses,
         "categories" : categories,
         "tags" : tags
         }


  return render(request, 'courses.html', context) 


def addComment(request,category_slug,id):
  course = get_object_or_404(Course, id = id)

  if request.method == "POST":
      comment_user = request.user
    #   comment_description = request.POST.get("comment_description")
      comment_description=request.POST.get("comment_description",False)

      newComment = Comment(comment_user = comment_user,comment_description = comment_description)

      newComment.course = course

      newComment.save()


   


  return redirect(reverse("course_detail", kwargs={"category_slug":category_slug,"course_id" : id}))


def course_learn(request,category_slug, course_id):
    
    course = Course.objects.get(category__slug=category_slug, id = course_id)

    
    return render(request,"learn.html",course)



