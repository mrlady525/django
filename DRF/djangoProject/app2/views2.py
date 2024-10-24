from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
#
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
@api_view(['GET'])
def get_data(request):
    """
    get请求
    :param request:
    :return:
    """
    return Response({'code':'success'},status=status.HTTP_200_OK)
@api_view(['POST', 'PUT', 'DELETE'])
def add_data(request):
    """
    post请求
    :param request:
    :return:
    """
    return Response({'code':'success'},status=status.HTTP_200_OK)

class DemoView(APIView):
    def get(self, request):
        return Response({'测试get'})
    def post(self, request):
        return Response({'post'})
    def put(self, request):
        return Response(['put'])
    def delete(self, request):
        return Response()