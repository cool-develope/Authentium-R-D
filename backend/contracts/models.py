from django.db import models

# Create your models here.

class Account(models.Model):
    name        = models.CharField(max_length=128, unique=True)
    address     = models.CharField(max_length=128, primary_key=True)
    ethers      = models.IntegerField()
    tokens      = models.IntegerField()
    platform    = models.CharField(max_length=128)