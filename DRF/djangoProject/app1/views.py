from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
class User_ListView(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset=UserInfo.objects.all()
    serializer_class=UserInfoSerializer
    def get(self,request,*args,**kwargs):
        # users = self.get_queryset()  ##GenericAPIView的方法，获取列表视图的查询集
        # ser = self.get_serializer(users, many=True)  ##GenericAPIView的方法，获取序列化器
        # return Response({'code': 200, 'data': ser.data, 'message': "OK"}, status=status.HTTP_200_OK)
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        # data = JSONParser().parse(request)
        # ser = self.get_serializer(data=data)  ##GenericAPIView的方法，获取序列化器
        # if ser.is_valid():
        #     ser.save()
        #     return Response({'code': 201, 'data': ser.data, 'message': "OK"}, status=status.HTTP_201_CREATED)
        # return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request,*args,**kwargs)

# @api_view(['GET','POST'])
# def user_list(request,format=None):
#  if request.method == 'GET':
#      # 返回用户列表
#      users = UserInfo.objects.all()
#      serializer = UserInfoSerializer(users, many=True)
#      return Response({'code':200,'data':serializer.data,'message':"OK"},status=status.HTTP_200_OK)
#  elif request.method == 'POST':
#      # 添加用户信息
#      data = JSONParser().parse(request)
#      serializer = UserInfoSerializer(data=data)
#      if serializer.is_valid():
#          serializer.save()
#          return Response({'code':201,'data':serializer.data,'message':"OK"}, status=status.HTTP_201_CREATED)
#      return Response({'code':400,'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class User_DetailView(GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    # def get_object(self,  id):
    #     try:
    #         return self.model.objects.get(id=id)
    #     except self.model.DoesNotExist:
    #         raise status.HTTP_404_NOT_FOUND
    def get(self,request,*args,**kwargs):
        # user=self.get_object() ##GenericAPIView的方法，获取单一对象（详细视图的对象实例），不需要传id
        # ser  = self.get_serializer(user)  ##GenericAPIView的方法，获取序列化器
        # return Response({'code': 200, 'data': ser.data, 'message': "OK"}, status=status.HTTP_200_OK)
        return self.retrieve(request,*args,**kwargs)
    def put(self, request,*args,**kwargs):
        # user=self.get_object()
        # data = JSONParser().parse(request)
        # ser = self.get_serializer(user, data=data)
        # if ser.is_valid():
        #     ser.save()
        #     return Response({'code': 200, 'data': ser.data, 'message': "OK"}, status=status.HTTP_200_OK)
        # return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)
        return self.update(request,*args,**kwargs)
    def delete(self, request,*args,**kwargs):
        # user=self.get_object()
        # user.delete()
        # return Response({'code': 204, 'message': "OK"}, status=status.HTTP_204_NO_CONTENT)
        return self.destroy(request,*args,**kwargs)

#===================收货地址增删查改==============

# @api_view(['GET','PUT','DELETE'])
# def user_detail(request, id,format=None):
#  """
#  获取单个用户、修改用户信息、删除用户信息
#  """
#  try:
#      user = UserInfo.objects.get(id=id)
#  except UserInfo.DoesNotExist:
#      return Response({'code':404,'message':"404,访问资源不存在"},status=status.HTTP_404_NOT_FOUND)
#  if request.method == 'GET':
#      serializer = UserInfoSerializer(user)
#      return Response({'code':200,'data':serializer.data,'message':"OK"},status=status.HTTP_200_OK)
#  elif request.method == 'PUT':
#      data = JSONParser().parse(request)
#      serializer = UserInfoSerializer(user, data=data)
#      if serializer.is_valid():
#          serializer.save()
#          return Response({'code':200,'data':serializer.data,'message':"OK"},status=status.HTTP_200_OK)
#      return Response({'code':200,'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#  elif request.method == 'DELETE':
#      user.delete()
#      return Response({'code':204,'message':"OK"},status=status.HTTP_204_NO_CONTENT)