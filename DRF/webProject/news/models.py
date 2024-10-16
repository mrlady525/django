from django.db import models

# Create your models here.
class NewsInfo(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    b_date = models.DateField()