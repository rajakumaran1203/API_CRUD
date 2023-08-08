from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    age = models.IntegerField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class StoredData(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key