from django.db import models
from django.db import models

# Create your models here.

#Destination
class Destination(models.Model):
    name  = models.CharField(max_length=100)
    price = models.IntegerField()
    dec   = models.TextField()
    img   = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)
   