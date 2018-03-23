from django.shortcuts import render
from .models import Post

def feed(request):
    posts=Post.objects.all()
    return render(request,'all_articles.html',{'posts':posts})


# Create your views here.
