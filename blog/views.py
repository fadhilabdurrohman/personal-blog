from django.shortcuts import render
from .models import Tag, Post

# Create your views here.

def show_post(request):
    posts = Post.objects.all().order_by('-created_at')
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'tags': tags,
    }

    return render(request, 'post_list.html', context)
