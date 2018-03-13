from django.shortcuts import render
from blog.models import Blog
# Create your views here.
def get_index(request):

    return render(request, 'home/index.html')