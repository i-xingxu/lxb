#coding=utf-8
from django.db import models

# Create your models here.

class myweb(models.Model):
    img_tittle = models.CharField(max_length = 20)
    img_desc = models.CharField(max_length = 50)
    img_path = models.CharField(max_length = 100)
    create_time = models.DateTimeField(auto_now_add = True)
    image = models.ImageField('图片', upload_to='images', blank=True)

    def __unicode__(self):
        return self.img_tittle,self.img_desc,self.img_path,self.create_time