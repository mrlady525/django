from django.urls import path,include
from app1 import views
from rest_framework.urlpatterns import format_suffix_patterns  ##支持url添加后缀

urlpatterns = [
    path('users/', views.User_ListView.as_view()),
    path('users/<int:id>/', views.User_DetailView.as_view()),
]

urlpatterns =format_suffix_patterns(urlpatterns)