from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=20,verbose_name='Nombre')
    last_name = models.CharField(max_length=20,verbose_name='Apellido')
    age = models.IntegerField(verbose_name='Edad')
    email = models.EmailField(verbose_name='Correo')
    phone = models.IntegerField(verbose_name='Telefono')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.name