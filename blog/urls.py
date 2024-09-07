from django.urls import path
from . import views

urlpatterns = [
    
    path('home', views.home, name='home'),
    
    path('post/', views.post, name='home'),
    
    path('post/<int:id>', views.post_by_id, name='post_by_id'),
    
    path('home/<int:id>/', views.google, name='google'),

]         