from django.shortcuts import render
from lxb_blog.models import Article

# Create your views here.

def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'index.html')