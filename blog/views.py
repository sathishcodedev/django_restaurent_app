from django.shortcuts import render
from .models import Post



# first view testing how its work
def index(request):
    #all data get from database post_table
    posts = Post.objects.all()

    category = request.GET.get('category')
    if category:
        post_category = Post.objects.filter(category = category)
    else:
        post_category = Post.objects.all()[:12]
    return render(request, 'index.html',{'posts':post_category, 'post':posts})


def detailview(request, id):

    posts = Post.objects.all()
    
    detail_category = Post.objects.filter(category=id)

    return render(request, 'detail.html', {'posts':detail_category})