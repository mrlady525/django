from django.urls import path
from .views import index

urlpatterns = [
    # http://域名(ip:端口)/news/index
    path('index', index)
]