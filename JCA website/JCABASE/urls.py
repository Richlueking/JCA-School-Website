from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('news/', views.news, name="news"),
    path('news_detail/<str:pk>/', views.news_details, name="news_detail"),

    path('blogs/', views.blog, name="blogs"),
    path('blog/<str:pk>/', views.blogDetails, name="blog"),

    path('news_form/', views.newsForm, name="news_form"),
    path('blog_form/', views.blogForm, name="blog_form"),
    path('contact/', views.contact, name='contact'),
]

