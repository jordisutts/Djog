from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import ComposeBlogForm

# Create your views here.

def get_inbox(request):
    return render(request, "blog/inbox.html")

def sent(request):
    return render(request, "blog/sent.html")
    
def view_message(request, id):
    message = get_object_or_404(Blog, pk=id)
    message.read = True
    message.save()
    return render(request, "blog/view_message.html", {'message': message})
    
def compose_message(request):
    if request.method == "POST":
        form = ComposeBlogForm(request.POST)
        message = form.save(commit=False)
        message.sender = request.user
        message.save()
        return redirect('inbox')
    else:
        form = ComposeBlogForm()
    
    return render(request, "blog/compose_message.html", {'form': form})