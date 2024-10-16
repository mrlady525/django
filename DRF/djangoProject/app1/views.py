from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import UserInfo
from .serializers import UserInfoSerializer


# Create your views here.
def user_list(request):
 if request.method == 'GET':
     # 返回用户列表
     users = UserInfo.objects.all()
     serializer = UserInfoSerializer(users, many=True)
     return JsonResponse(serializer.data, safe=False)
 elif request.method == 'POST':
     # 添加用户信息
     data = JSONParser().parse(request)
     serializer = UserInfoSerializer(data=data)
     if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, status=201)
     return JsonResponse(serializer.errors, status=400)


def user_detail(request, id):
 """
 获取单个用户、修改用户信息、删除用户信息
 """
 try:
     user = UserInfo.objects.get(id=id)
 except UserInfo.DoesNotExist:
     return HttpResponse(status=404)
 if request.method == 'GET':
     serializer = UserInfoSerializer(user)
     return JsonResponse(serializer.data)
 elif request.method == 'PUT':
     data = JSONParser().parse(request)
     serializer = UserInfoSerializer(user, data=data)
     if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data)
     return JsonResponse(serializer.errors, status=400)
 elif request.method == 'DELETE':
     user.delete()
     return HttpResponse(status=204)