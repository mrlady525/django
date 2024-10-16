"""
定义DRF框架的序列化器类

"""
from rest_framework import serializers

from app1.models import UserInfo


class UserInfoSerializer(serializers.Serializer):
    """定义序列化器"""
    name=serializers.CharField(max_length=20)
    pwd=serializers.CharField(max_length=18)
    email=serializers.EmailField(max_length=254)
    age=serializers.IntegerField(default=18,min_value=0,max_value=150)
    id=serializers.IntegerField(read_only=True)  ##只参与序列化，不参与反序列化的校验
    def create(self,validated_data):
        """自定义一个序列化器保存数据的方法"""
        return UserInfo.objects.create(**validated_data)
    def update(self,instance,validated_data):
        """序列化器修改数据的方法"""
        instance.name=validated_data['name']
        instance.pwd=validated_data['pwd']
        instance.email=validated_data['email']
        instance.age=validated_data['age']
        instance.save()
        return instance

class AddrSerializer(serializers.Serializer):
    """定义序列化器"""
    mobile = serializers.CharField( max_length=18)
    city = serializers.CharField(max_length=10)
    info = serializers.CharField(max_length=200)
    #返回关联对象的序列化器
    user=serializers.PrimaryKeyRelatedField(queryset=UserInfo.objects)