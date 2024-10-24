from django.db import models

# Create your models here.
"""
DRF序列化：
    json序列化：将一个python对象，转化为一个json对象（json字符串）
DRF反序列化：
    json反序列化：将一个json对象，转化为一个python ORM对象，保存到数据库
"""
class UserInfo(models.Model):
    """用户信息模型"""
    name=models.CharField(max_length=20,verbose_name='用户名')
    pwd=models.CharField(max_length=18,verbose_name='密码', blank=False, null=False)
    email=models.EmailField(max_length=254,verbose_name='邮箱')
    age=models.IntegerField(verbose_name='年龄',default=18)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'userinfo'
        verbose_name = '用户信息'

class Addr(models.Model):
    """收货地址模型"""
    user=models.ForeignKey('UserInfo',verbose_name='所属用户',on_delete=models.CASCADE)
    mobile = models.CharField(verbose_name='手机号', max_length=18)
    city = models.CharField(verbose_name='城市', max_length=10)
    info = models.CharField(verbose_name='详细地址', max_length=200)

    def __str__(self):
        return self.info