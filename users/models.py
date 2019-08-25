from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_lenght=50)
    phone = models.CharField(max_lenght=50)
#Phone = {ddd:00,number1:00000,number2:0000}