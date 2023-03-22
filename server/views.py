from django.shortcuts import render
from .models import *


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
