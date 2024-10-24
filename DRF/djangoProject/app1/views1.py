from django.db.migrations import serializer
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from .models import UserInfo
from .serializers import UserInfoSerializer


# Create your views here.

def user_list(request):
    """
    get 方法请求：获取用户列表
    post方法请求：添加用户信息
    :param request:
    :return:
    """
    #判断请求方法：
    if request.method == "GET":
        """
        1、获取用户列表并返回，查询所有用户信息
        2、创建序列化对象 
        """
        user_list = UserInfo.objects.all()
        ser = UserInfoSerializer(user_list, many=True)
        return JsonResponse({"code": 200, "data":ser.data,"msg": "success"},status=200)
    elif request.method == "POST":
        """
        1、加一条用户信息
        2、创建序列化器,并校验数据
        3、校验通过则添加数据到数据库；校验失败，则返回错误
        """
        params = JSONParser().parse(request)
        ser=UserInfoSerializer(data=params)
        if ser.is_valid():
            #校验通过则添加数据到数据库
            ser.save()
            return JsonResponse({"code": 201, "data":ser.data,"msg": "添加成功！"})
        else:
            #校验失败，则返回错误
            return JsonResponse({"code": 400, "data": ser.data, "msg": ser.errors})
    else:
        return JsonResponse({"code": 405, "msg": "当前不支持请求方法{}".format(request.method)})

def user_detail(request,id):
    """
    GET:获取单个用户信息
    PUT:修改用户信息
    DELETE：删除用户
    :param request:
    :param id:
    :return:
    """
    try:
        obj = UserInfo.objects.get(id=id)
    except Exception as e:
        return HttpResponse('404,访问资源不存在',status=404)
    if request.method == "GET":
        ser = UserInfoSerializer(obj)
        return JsonResponse({'code': 200, 'data': ser.data, 'msg': 'success'},status=200)
    elif request.method == "DELETE":
        obj.delete()
        return JsonResponse({}, status=204)
    elif request.method == "PUT":
        ##添加一条用户信息，#创建序列化器,并校验数据，校验通过就保存
        data = JSONParser().parse(request)
        ser = UserInfoSerializer(obj, data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.errors, status=400)
    else:
        return JsonResponse({"code": 405, "msg": "当前不支持请求方法{}".format(request.method)})
