"""
定义DRF框架的序列化器类

"""
from rest_framework import serializers

from .models import UserInfo,Addr

class UserInfoSerializer(serializers.Serializer):
    """定义序列化器"""
    name=serializers.CharField(max_length=20)
    pwd=serializers.CharField(max_length=18)
    email=serializers.CharField(max_length=254)
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


class UserInfoSerializer(serializers.ModelSerializer):  ##模型序列化器包含了默认的create()和update()的实现；基于模型类自动为Serializer生成validators，比如unique_together
    class Meta:
        model = UserInfo
        fields = '__all__'
    # def validate_pwd(self,value):
    #     ##自定义的字段校验器
    #     if not(6<len(value)<18):
    #         raise serializers.ValidationError('密码长度需要在6-18位之间')

class AddrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addr
