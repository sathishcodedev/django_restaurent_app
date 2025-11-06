from django.shortcuts import render
from .models import Post




# first view testing how its work
def index(request):
    posts = Post.objects.all()

    return render(request, 'index.html',{'posts':posts})