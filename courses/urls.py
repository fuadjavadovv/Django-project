from django.urls import path
from courses import views



urlpatterns = [
    path('', views.course_list, name="courses"),
    path("<slug:category_slug>/<int:course_id>", views.course_detail, name='course_detail'),
    path("<slug:category_slug>/<int:course_id>/", views.course_learn, name='course_learn'),  
    path("categories/<slug:category_slug>", views.course_list, name='courses_by_category'), 
    path("tag/<slug:tag_slug>", views.course_list, name='courses_by_tag'), 
    path("search/", views.search, name='search'), 
    path("<slug:category_slug>/comment/<int:id>/", views.addComment, name='comment'), 
]
#course_detail bunu orda yazmag lazim deyildi cunki onsuzda biz o linkin icinde olurug