from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from teachers.models import Teacher
from django.views.generic.detail import DetailView
from courses.models import Course
# Create your views here.
class TeacherListView(ListView):
    model = Teacher
    template_name = "teachers.html"
    paginate_by = 3


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = "teacher.html"
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(avilable=True, teacher= self.kwargs['pk'])
        return context