from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255) #esto se traduce a la base de datos como varchar(255).
    description = models.TextField() #no tiene un valor maximo de carácteres.
    price = models.DecimalField(max_digits=6,decimal_places=2) #este es mejor usarlo que float ya que float tiene problemas de redondeo.
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)

class Customer(models.Model):
    fist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birdth_date = models.DateField(null=True) #la fecha de nacimiento podrá dejarse en vacio.

#LOS ID´S SE CREAN AUTOMÁTICAMENTE.





    


