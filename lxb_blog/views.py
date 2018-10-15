#coding=utf-8
from django.shortcuts import render
from lxb_blog.models import myweb
from lxb_blog.forms import CureDataImageForm
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.conf import settings
import os
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
        # form = CureDataImageForm(request.POST or None, request.FILES or None)
        # if form.is_valid():
        if image.size>0:
            # image = request.FILES.get('images')
            # image.save()
            path=default_storage.save("images/"+image.name,ContentFile(image.read()))
            tmp_file=os.path.join(settings.MEDIA_ROOT,path)
            # print(image.image.url)

            return HttpResponseRedirect('/')
    # else:
    #     form = CureDataImageForm()
    # return render(request,'upload.html', {'form': form})
    # return  render(request,{'form':form})
    # return render(request, 'upload.html')

def love_time(request):

    return render(request,'index.html')


