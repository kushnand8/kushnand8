from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class AddPost(models.Model):
    title = models.CharField(max_length=175)
    pst = models.TextField()
    un = models.CharField(max_length=100)

class AddComment(models.Model):
    post = models.ForeignKey(AddPost, related_name='AddComment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='AddComment', on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    comment = models.TextField()

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)
