from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {'posts': posts})
    
    
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    return render(request, "blog/post_detail.html", {'post': post})


def edit_post(request, id):
    item = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    form = PostForm(instance=item)
    return render(request, "blog/post_edit.html", { 'form': form })


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("post_list")
    form = PostForm()
    return render(request, "blog/create_post.html", { 'form': form })