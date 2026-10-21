from .forms import PostForm
from .models import Tag, Post
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def show_post(request):
    posts = Post.objects.all().order_by('-created_at')
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'tags': tags,
    }

    return render(request, 'post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'post.html', {'post': post})

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('blog:post_list')

    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('blog:post_list')

@login_required(login_url="/login/")
def create_post(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('blog:post_list')

    return render(request, 'post_form.html', {'form': form})

@login_required(login_url="/login/")
def update_post(request, pk):
    if not request.user.is_superuser:
        raise PermissionDenied

    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('blog:post', pk=pk)

    return render(request, 'post_form.html', {'form': form, 'post': post})

@login_required(login_url="/login/")
def delete_post(request, pk):
    if not request.user.is_superuser:
        raise PermissionDenied

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')

    return render(request, 'post_delete_confirm.html', {'post': post})