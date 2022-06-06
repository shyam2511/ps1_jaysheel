from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    campus = models.CharField(max_length=50)
