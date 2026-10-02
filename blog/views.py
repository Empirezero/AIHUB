from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from rest_framework import viewsets
from .serializers import PostSerializer


def home(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blog/post_detail.html', {'post': post})


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer