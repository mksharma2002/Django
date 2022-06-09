from django.shortcuts import render
from .models import BlogPost

from django.http import HttpResponse

def index(request):
    myposts = BlogPost.objects.all()

    return render(request, "blog/index.html", {'myposts':myposts})


def blogpost(request, id):
    post = BlogPost.objects.filter(post_Id = id)[0]
    return render(request, "blog/blogpost.html",{'post': post})
    

# Create your views here.
