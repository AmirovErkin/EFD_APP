from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=100)
