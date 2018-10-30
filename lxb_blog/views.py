#coding=utf-8
from django.shortcuts import render
from lxb_blog.models import myweb
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect
import os
import time
# Create your views here.

def home(request):
    imageInfo = myweb.objects.all()  #获取全部的Article对象
    context={}
    context["imagePath"] = ""
    context["imageTittle"] = ""
    context["imageDesc"] = ""
    context["createTime"] = ""

    contexts=[]
    for i in imageInfo:
        context["imagePath"]="../static/"+str(i.image)
        context["imageTittle"]=i.img_tittle
        context["imageDesc"]=i.img_desc
        context["createTime"]=i.create_time
        contexts.append(context.copy())

    return render(request, 'photo.html',{"imageInfo":contexts})
@csrf_exempt
def upload(request):
    if request.method =="GET":
        return render(request, 'upload.html')

    if request.method == 'POST':
        image=request.FILES.get("fileList")
        if image.size>0:
            path=default_storage.save("images/"+image.name,ContentFile(image.read()))
            tmp_file=os.path.join(settings.MEDIA_ROOT,path)
            picInfo={}
            picInfo["img_desc"]=request.POST["description"]
            picInfo["img_time"]=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            picInfo["img_path"]=path
            myweb().insert_into_description(picInfo)

            return HttpResponseRedirect('')
            # return  redirect('/photo/')

def love_time(request):

    return render(request,'index.html')


