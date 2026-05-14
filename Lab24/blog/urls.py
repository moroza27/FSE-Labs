from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('media/', views.media_view, name='blog-media'),
]