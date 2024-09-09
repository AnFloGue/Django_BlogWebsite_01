from django.urls import path
from . import views

app_name = 'blog'  # Define the namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('post/<int:id>/', views.post_by_id, name='post_by_id'),
    path('google/<int:id>/', views.google, name='google'),
]