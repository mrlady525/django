from django.contrib import admin
from django.urls import path,include
from app2 import views,views2

urlpatterns = [
    path('getdata/',views.get_data),
    path('adddata/',views.add_data),
    path('demo/',views2.DemoView.as_view()),
]
