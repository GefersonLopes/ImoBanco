from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=255)