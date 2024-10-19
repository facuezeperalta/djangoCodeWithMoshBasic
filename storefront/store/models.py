from django.db import models

# Create your models here.
#promtion * ----- * product
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
class Collection(models.Model):
    title = models.CharField(max_length=255)
    feature_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True,related_name='+') #El + le indica a Django que no cree la relación inversa 

class Product(models.Model):
    title = models.CharField(max_length=255) #esto se traduce a la base de datos como varchar(255).
    description = models.TextField() #no tiene un valor maximo de carácteres.
    price = models.DecimalField(max_digits=6,decimal_places=2) #este es mejor usarlo que float ya que float tiene problemas de redondeo.
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey('Collection',on_delete=models.PROTECT) #primero referenciamos a la clase padre, si la clase padre no esta antes en el código podemos poner el valor entre '' como una string para evitar errores. Se pone en modo PROTECT para no borrar todo una vez elimine un producto no se elimine la colección entera de productos.
    promotions = models.ManyToManyField(Promotion) 

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold')
    ]
    fist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birdth_date = models.DateField(null=True) #la fecha de nacimiento podrá dejarse en vacio.
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
#LOS ID´S SE CREAN AUTOMÁTICAMENTE.

class Order(models.Model):
    PAYMENT_STATUS_PENDING  = 'P'
    PAYMENT_STATUS_COMPLETE= 'C'
    PAYMENT_STATUS_FAIL= 'F'
    PAYMENT_STATUS_CHOICES =[
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAIL,'Fail')
    ]
    place_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT) #Si borramos un cliente no queremos borrar las ordenes. Esto NUNCA debería pasar.

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)  #Esto es para guardar el precio del producto al momneto de hacer la orden.

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    #Se debe especificar el padre
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE, primary_key=True) #opciones que también podemos usa set_default, protect. El valor que usamos depende del requerimiento. 

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
