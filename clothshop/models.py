from django.db import models

# Create your models here.
class Product(models.Model):
    Name=models.CharField(max_length=250)
    Price=models.FloatField()
    Stock=models.IntegerField()
    Image=models.CharField(max_length=2500)