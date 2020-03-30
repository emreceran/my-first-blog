from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User


def post_list(request):
    #mecburi yorum
    ben = User.objects.get(username='emre')

    posts = Post.objects.filter(author=ben).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
