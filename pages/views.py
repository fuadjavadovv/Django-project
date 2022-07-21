
from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from courses.models import Course
from teachers.models import Teacher
from courses.views import course_detail
from django.contrib.auth.models import User
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import F
# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['courses'] = Course.objects.filter(avilable=True).order_by('-date')[:2]
      context['total_course'] = Course.objects.filter(avilable=True).count()
      context['total_teacher'] = Teacher.objects.filter().count()
      context['total_user'] = User.objects.filter().count()
      context['total_users'] = User.objects.filter().count()+1
   
      return context




# def index(request):
#     return render(request,"index.html")
    


class AboutView(TemplateView):
       model = Teacher
       template_name = 'about.html'
       context_object_name = 'teacher'
      

# def about(request):
#     return render(request,"about.html")    

class ContactView(SuccessMessageMixin,FormView):
      template_name = 'contact.html'
      form_class = ContactForm
      success_url = reverse_lazy('contact')
     
      

      def form_valid(self,form):
             form.save()
             return super().form_valid(form)