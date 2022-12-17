from django.db import models

# Create your models here.
class Cafeteria(models.Model):
    id = models.AutoField(primary_key= True)
    clasificacion = models.CharField(max_length=30, blank= False, null = False)
    producto = models.CharField(max_length=30, blank= False, null = False)
    marca = models.CharField(max_length=30, blank= False, null = False)
    precio = models.IntegerField()
    image = models.CharField(max_length = 150, blank = False, null = False)

 

   
