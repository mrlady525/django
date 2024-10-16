from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import NewsInfo
class NewsInfoAdmin(admin.ModelAdmin):
    # list_display表示要显示哪些属性
    list_display = ['id','title','b_date']
admin.site.register(NewsInfo,NewsInfoAdmin)