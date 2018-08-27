#coding=utf-8
from django.shortcuts import render
from lxb_blog.models import myweb
from lxb_blog.forms import CureDataImageForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
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
    if request.method == 'POST':

        form = CureDataImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            image = form.save()
            print(image.image.url)

            # return HttpResponseRedirect('/mysite/success/')
    else:
        form = CureDataImageForm()
    # return render_to_response('mysite/data_form.html', {'form': form})
    return  render(request,'upload.html',{'form':form})


def love_time(request):

    return render(request,'index.html')

