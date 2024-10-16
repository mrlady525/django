from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsInfo
# Create your views here.

# def index(request):
#     return HttpResponse('这个是index页面')
def index(request):
    s_info = NewsInfo.objects.all()
    context={'title':'新闻列表','list':[item.title for item in s_info]}
    return render(request,'news/index.html',context)