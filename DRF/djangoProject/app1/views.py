from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def user_list(request):
 if request.method == 'GET':
     # 返回用户列表
     users = UserInfo.objects.all()
     serializer = UserInfoSerializer(users, many=True)
     return Response({'code':200,'data':serializer.data,'message':"OK"},status=status.HTTP_200_OK)
 elif request.method == 'POST':
     # 添加用户信息
     data = JSONParser().parse(request)
     serializer = UserInfoSerializer(data=data)
     if serializer.is_valid():
         serializer.save()
         return Response({'code':201,'data':serializer.data,'message':"OK"}, status=status.HTTP_201_CREATED)
     return Response({'code':400,'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail(request, id):
 """
 获取单个用户、修改用户信息、删除用户信息
 """
 try:
     user = UserInfo.objects.get(id=id)
 except UserInfo.DoesNotExist:
     return Response({'code':404,'message':"404,访问资源不存在"},status=status.HTTP_404_NOT_FOUND)
 if request.method == 'GET':
     serializer = UserInfoSerializer(user)
     return Response({'code':200,'data':serializer.data,'message':"OK"},status=status.HTTP_200_OK)
 elif request.method == 'PUT':
     data = JSONParser().parse(request)
     serializer = UserInfoSerializer(user, data=data)
     if serializer.is_valid():
         serializer.save()
         return Response({'code':200,'data':serializer.data,'message':"OK"},status=status.HTTP_200_OK)
     return Response({'code':200,'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
 elif request.method == 'DELETE':
     user.delete()
     return Response({'code':204,'message':"OK"},status=status.HTTP_204_NO_CONTENT)