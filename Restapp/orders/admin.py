from django.contrib import admin
from .views import Product,Order
from .models import Restaurant,Table,Booking
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Restaurant)
admin.site.register(Table)

admin.site.register(Booking)
