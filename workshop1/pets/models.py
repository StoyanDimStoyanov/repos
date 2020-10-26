from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from authentication.forms import CreateUserFrom


class Pet(models.Model):
    DOG = "Dog"
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'Unknow'

    PET_TYPES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown')
    )

    type = models.CharField(max_length=7, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField(blank=True, max_length=100)
    image_url = models.URLField(blank=False, )
    date_created = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ', '.join((self.name, str(self.age)))


class Like(models.Model):
    user_who_liked = models.CharField(blank=False, max_length=8, default='')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
