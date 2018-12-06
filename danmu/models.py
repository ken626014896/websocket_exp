from django.db import models

# Create your models here.
class DanmuModel(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    send_time=models.CharField(max_length=50)
    send_time_float=models.FloatField(null=True,blank=True)