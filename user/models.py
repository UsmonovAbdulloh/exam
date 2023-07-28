from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','Admin'),
        ('u','User'),
        ('o','Owner')
    )
    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)

class PersonModel(models.Model):
    name = models.CharField(max_length=65,default='')
    fname = models.CharField(max_length=65,default='')
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class UserModel(PersonModel):
    phone = models.CharField(max_length=25,default='')
    password = models.CharField(max_length=40,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'User'

