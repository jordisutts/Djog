from django.shortcuts import render
from messenger.models import Message
# Create your views here.
def get_index(request):

    return render(request, 'home/index.html')