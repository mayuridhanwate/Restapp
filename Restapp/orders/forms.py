from django.forms import ModelForm
from django import forms
from .models import Order, Product


class OrderForm(ModelForm):
    OPTIONS = (
        ('Postpay', 'Postpay'),
        ('Prepay (Full)', 'Prepay (Full)'),
        ('Prepay (Half)', 'Prepay (Half)')
    )
    OPTIONS2 = (
        ('Confirm', 'Confirm'),
        ('Ready', 'Ready'),
        ('Send', 'Send'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled')
    )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=OPTIONS)
    #TEST_CHOICES = [[x.id, x.product_name] for x in Product.objects.all()]
    #TEST_CHOICES = [[x.id, x.product_name] for x in Product.objects.all()]
    #product_id = forms.ModelChoiceField(queryset=Product.objects.filter(active='1'), empty_label='')
    product_id = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    #product_id = forms.MultipleChoiceField(choices=TEST_CHOICES, widget=forms.CheckboxSelectMultiple())

    delivery_date = forms.DateField(required=True)
    quantity = forms.IntegerField(initial=0)

    class Meta:
        model = Order
        fields = ['name','phone','address','delivery_date','product_id','payment_option','quantity','order_status']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_details','price','type']

from django import forms
from django.contrib.auth.models import User

class loginForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
         model = User
         fields = ['email', 'password']



from orders.models import Restaurant,Booking,Table
from django.forms import ModelForm

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = [ 'name', 'description',  'opening_time', 'closing_time']

class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ['restaurant', 'size']

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'people', 'booking_date_time_start', 'booking_date_time_end']
