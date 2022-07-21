
from django.urls import path, include
from api import view as api_views

urlpatterns = [
    path('course/',api_views.CourseListCreateAPIView.as_view(), name = 'course' ),
    path('course/<int:pk>',api_views.CourseDetailAPIView.as_view(), name = 'course-detail' ),
    path('teacher/',api_views.TeacherCreateApiView.as_view(), name = 'teacher' ),
    path('comment/<int:pk>',api_views.CommentDetailApiView.as_view(), name = 'comment' ),
    


] 
