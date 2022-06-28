from statistics import mode
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=254)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=254) 
class Offers(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=254)
    discount = models.FloatField()

