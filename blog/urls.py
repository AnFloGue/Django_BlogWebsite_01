from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/<id>', views.post, name='post'),
]