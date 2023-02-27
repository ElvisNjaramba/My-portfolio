from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Message(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    message = models.TextField(max_length=10000)