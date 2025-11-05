from django.shortcuts import render

# Create your views here.
# first view testing how its work
def index(request):
    return render(request, 'base.html')