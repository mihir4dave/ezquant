from django.contrib.auth.models import AbstractUser, GroupManager, User
from django.contrib.auth.models import Group as BaseGroup
from django.db import models

class usertype(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    type= models.CharField(max_length=30)
