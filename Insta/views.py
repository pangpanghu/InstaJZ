from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

#继承了TemplateView 这个类，基本功能都有了
#settting 已经定义Template 的路径。所以这里只要给HTML 文件的名字就好了
class HelloDjango(TemplateView):
    template_name = 'home.html'
