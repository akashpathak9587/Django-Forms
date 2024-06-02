from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='media')
    resume = models.FileField(upload_to='media')
    mobile_No = models.IntegerField()
    favorite_color = models.CharField(max_length=100)