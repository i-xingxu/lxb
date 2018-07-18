from django.shortcuts import render
from lxb_blog.models import myweb

# Create your views here.

def home(request):
    post_list = myweb.objects.all()  #获取全部的Article对象
    context={}
    data=myweb.objects.get(id=2)


    context["imagePath"]=[data.img_path]
    return render(request, 'index.html',context)
