from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='house'),
    path('post/', views.post, name='post'),
    path('post/<int:id>/', views.post_by_id, name='post_by_id'),
    path('google/<int:id>/', views.google, name='google'),
]