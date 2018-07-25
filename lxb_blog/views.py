#coding=utf-8
from django.shortcuts import render
from lxb_blog.models import myweb

# Create your views here.

def home(request):
    imageInfo = myweb.objects.all()  #获取全部的Article对象
    context={}
    # context["imagePath"] = []
    # context["imageTittle"] = []
    # context["imageDesc"] = []
    # context["createTime"] = []

    contexts=[]
    for i in imageInfo:
        context["imagePath"]=i.img_path
        context["imageTittle"]=i.img_tittle
        context["imageDesc"]=i.img_desc
        context["createTime"]=i.create_time
        contexts.append(context)

    return render(request, 'index.html',{"imageInfo":contexts})
