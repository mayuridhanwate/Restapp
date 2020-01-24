from django.db import models

# Create your models here.
class Product(models.Model):
    FOOD_TYPES = (
        ('appetizer', 'appetizer'),
        ('entree', 'entree'),
        ('dessert', 'dessert'),
        ('sandwich', 'sandwich'),
        ('drinks', 'drinks'),

    )
    type = models.CharField(max_length=100, choices=FOOD_TYPES,blank=True,null=True)
    product_name = models.CharField(max_length=200)
    product_details = models.TextField()
    price = models.IntegerField()
    active = models.IntegerField(default='1')

    def __str__(self):
        return '%s (%s tk)' % (self.product_name, self.price)

class Order(models.Model):


    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    delivery_date = models.DateField(blank=True)
    #product_id = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    product_id = models.ManyToManyField(Product)
    payment_option = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    quantity = models.IntegerField()

class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    opening_time = models.IntegerField()
    closing_time = models.IntegerField()


class Table(models.Model):
    choice = (('R', 'Reserved'), ('Non', 'Non_Reserved'))

    restaurant = models.ForeignKey(Restaurant,on_delete='models.CASCADE',null=True)
    size = models.IntegerField()
    # select_choice2 = ["Vegeterian", "Non_Vegeterian"]
    status = models.CharField(max_length=50, blank=True, choices=choice)

class Booking(models.Model):
    table = models.ForeignKey(Table,on_delete='models.CASCADE',null=True)
    people = models.IntegerField()
    booking_date_time_start = models.DateTimeField()
    booking_date_time_end = models.DateTimeField()

