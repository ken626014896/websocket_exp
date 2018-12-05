from django.db import models

# Create your models here.
class ExpModel(models.Model):
     name=models.CharField(max_length=50)
     message=models.CharField(max_length=50)