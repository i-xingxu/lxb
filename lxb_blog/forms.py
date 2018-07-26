#coding=utf-8

from django import forms
from .models import myweb

class CureDataImageForm(forms.ModelForm):

    class Meta:
        model = myweb
        # fields = '__all__'  # ['name', 'create_at',  ...]
        fields=('img_tittle','img_desc','image')