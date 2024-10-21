from django.contrib import admin
from django.urls import path,include
from app2 import views

urlpatterns = [
    path('getdata/',views.get_data),
    path('adddata/',views.add_data),
]
