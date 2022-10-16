from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
from django.utils import timezone

# Create your views here.
#camando o html da inicial 
def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':post})

# =================
# power query para ordenar os comentários 



