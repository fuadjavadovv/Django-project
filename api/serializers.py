from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from courses.models import Course,Comment
from teachers.models import Teacher



class CommentSerializer(serializers.ModelSerializer):
  comment_user = serializers.StringRelatedField()

  class Meta:
    model = Comment
    fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True,read_only=True)
  
  class Meta:
      model =  Course
      fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
  courses = CourseSerializer(many=True, read_only=True)

  courses = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'course-detail'
  )
  class Meta:
    model = Teacher
    fields = ["name","title","description","courses"]






