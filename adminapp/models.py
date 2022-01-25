from django.db import models

# Create your models here.


class adminlogin(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=20)


class position(models.Model):
    position = models.CharField(max_length=50)
