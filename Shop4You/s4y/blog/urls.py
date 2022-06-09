from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='bloghome'),
    path('blogpost/<int:id>', views.blogpost,name="bloghome"),
  
]
