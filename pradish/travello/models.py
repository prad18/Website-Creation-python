from django.db import models

# Create your models here.

#Destination
class Destination():
    id:int
    name:str
    price:int
    dec:str
    img:str
    offer=bool
   