from django.db import models


# Create your models here.
from pets.models import Pet


class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    username = models.CharField(max_length=30, default='')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
