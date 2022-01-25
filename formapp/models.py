from django.db import models

# Create your models here.


class Form(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=40)
