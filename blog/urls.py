from django.urls import path
from . import views

urlpatterns = [
    path('blog/helloworld', views.home, name='home'),
]