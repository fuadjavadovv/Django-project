from rest_framework import generics
from courses.models import Course,Comment
from teachers.models import Teacher
from .serializers import CourseSerializer,TeacherSerializer,CommentSerializer
from .pagination import LargeResultsSetPagination

class CourseListCreateAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = LargeResultsSetPagination



class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Course.objects.all()
     serializer_class = CourseSerializer


class TeacherCreateApiView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = LargeResultsSetPagination


class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CourseSerializer



