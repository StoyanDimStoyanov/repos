from django.db import models


class Users(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100, default="")
