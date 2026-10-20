from django.shortcuts import render, redirect
from .models import Tag, Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.

def show_post(request):
    posts = Post.objects.all().order_by('-created_at')
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'tags': tags,
    }

    return render(request, 'post_list.html', context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('main:post_list')

    return render(request, 'login.html', {'form': form})
