from django.shortcuts import render, redirect
from .models import Order, Product
from .forms import OrderForm, ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from orders.models import Table, Booking,Restaurant
@login_required
def index(request):
    orders = Order.objects.all()
    return render(request, 'index.html', {'orders': orders})

@login_required
def show(request, order_id):
    order = Order.objects.filter(id=order_id)
    return render(request, 'show.html', {'order': order})

@login_required
def new(request):
    if request.POST:
        form = OrderForm(request.POST)
        print (form.errors)
        if form.is_valid():

            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'new.html', {'form':form})

@login_required
def edit(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm(instance=order)
        return render(request, 'edit.html', {'form':form})

@login_required
def destroy(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('/', messages.success(request, 'Order was successfully deleted.', 'alert-success'))



#Product

@login_required
def index_product(request):
    products = Product.objects.filter(active='1')
    return render(request, 'index_product.html', {'products': products})    

@login_required
def new_product(request):
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/products', messages.success(request, 'Product was successfully created.', 'alert-success'))
            else:
                return redirect('/products', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/products', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        product_form = ProductForm()
        return render(request, 'new_product.html', {'product_form':product_form})    

@login_required
def destroy_product(request, product_id):
    #order = Order.objects.filter(product_id=product_id).count()

    #if order > 0:
    #     return redirect('/products', messages.success(request, 'Cannot delete product while its order exists.', 'alert-danger'))    
    #else:
    #    product = Product.objects.get(id=product_id)
    #    product.delete()
    #    return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))      

    if Product.objects.filter(id=product_id).update(active='0'):
        return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))  
    else:
        return redirect('/products', messages.danger(request, 'Cannot delete product while its order exists.', 'alert-danger'))

def AllMenu(request):
    products = Product.objects.all()
    item1 = Product.objects.values_list('type', flat=True).distinct()
    print(item1)
    print(products)


    return render(request, 'Menu.html', {'products': products,'item1': item1})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from .forms import loginForm

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('nuevoTurno.html')
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form})


#django.setup()

def index1(request):

    get = Table.objects.filter(status='Non_Reserved')
    print(get.count())

    restaurant = request.POST.get('restaurant')
    print("rest", restaurant)
    booking_date_time_start = request.POST.get('booking_date_time_start')
    print(booking_date_time_start)
    booking_date_time_end = request.POST.get('booking_date_time_end')
    people = request.POST.get('people')
    book_restaurant_table(request,restaurant, booking_date_time_start, people )


def _cache_index(self, database, collection, index, cache_for):
	"""Add an index to the index cache for ensure_index operations.
	"""
	now = datetime.datetime.utcnow()
	expire = datetime.timedelta(seconds=cache_for) + now

def book_restaurant_table(restaurant, booking_date_time, people, minutes_slot=90):
    """
    This method uses get_first_table_available to get the first table available, then it
    creates a Booking on the database.
    """
    table = get_first_table_available(restaurant, booking_date_time, people, minutes_slot)
    print(table)
    if table:
        print("Welcome")
        delta = timedelta(seconds=60 * minutes_slot)
        booking_date_time = datetime.datetime.strptime(booking_date_time, '%Y-%m-%d %H:%M:%S.%f');

        booking = Booking(table=table, people=people,
                          booking_date_time_start=booking_date_time, booking_date_time_end=booking_date_time + delta)
        booking.save()
        print(booking.id)
        print(table.id)
        context = {
            'booking': booking.id,
            'table': table.id,
        }
        return {'booking': booking.id, 'table': table.id}


        #return redirect('/', messages.success(request,'Successfully','alert-success'))
        #return redirect(request, 'index1.html')
        #return redirect('/products', messages.success(request, 'Product was successfully created.', 'alert-success'))
        # return HttpResponseRedirect(request, 'restaurants/index.html',{'booking': booking.id, 'table': table.id})
        #return HttpResponseRedirect('restaurants/index.html',messages.success(request,'Successfully'))
        #return render(request, 'index1.html', {'booking': booking.id, 'table': table.id})

    else:
        return None

#        return redirect('/products', messages.success(request, 'Product was successfully created.', 'alert-success'))
        #return render(request, 'index1.html')

        # return None


import datetime
from datetime import time,datetime,timedelta
import datetime

def get_first_table_available(restaurant, booking_date_time, people, minutes_slot=90):
    """
    This method returns the first available table of a restaurant, given a specific number of
    people and a booking date/time.
    """
    # I make sure to check if the tables are not already booked within the time slot required
    # by the new booking
    #m = Table.objects.all()
    #print(len(m))

    #print(type(booking_date_time))
    delta = timedelta(seconds=60*minutes_slot)
    #booking_date_time=datetime(booking_date_time)
    booking_date_time = datetime.datetime.strptime(booking_date_time,'%Y-%m-%d %H:%M:%S.%f');
    l_bound_time = booking_date_time
   # u_bound_time = booking_date_time +datetime.timedelta(minutes=15)
    u_bound_time= booking_date_time+delta
    tables_booked_ids = []

    # Exclude tables which start and end booking date includes requested initial booking date_time
    tables_booked = Booking.objects.filter(table__restaurant=restaurant,
        booking_date_time_start__lt=l_bound_time,
        booking_date_time_end__gt=l_bound_time).values('table')
    #print(tables_booked)
    for value in tables_booked:
        print(value.id)
    tables_booked_ids_temp = [x['table'] for x in tables_booked]
    tables_booked_ids = tables_booked_ids + tables_booked_ids_temp

    # Exclude tables which start and end booking date includes requested ending booking date_time
    tables_booked = Booking.objects.filter(
        booking_date_time_start__lt=u_bound_time,
        booking_date_time_end__gt=u_bound_time).values('table')
    #print(tables_booked)
    for value in tables_booked:
        print(value.id)

    tables_booked_ids_temp = [x['table'] for x in tables_booked]
    tables_booked_ids = tables_booked_ids + tables_booked_ids_temp

    # Exclude tables which booking slots is inside requested booking slot
    tables_booked = Booking.objects.filter(
        booking_date_time_start__gt=l_bound_time,
        booking_date_time_end__lt=u_bound_time).values('table')
    #print(tables_booked)
    for value in tables_booked:
        print(value.size)

    tables_booked_ids_temp = [x['table'] for x in tables_booked]
    tables_booked_ids = tables_booked_ids + tables_booked_ids_temp

    # Exclude tables which include requested booking slot
    tables_booked = Booking.objects.filter(
        booking_date_time_start__lt=l_bound_time,
        booking_date_time_end__gt=u_bound_time).values('table')
    print(len(tables_booked))
    #print(tables_booked[0].table)
    for value in tables_booked:
        print(value.table)

    tables_booked_ids_temp = [x['table'] for x in tables_booked]
    tables_booked_ids = tables_booked_ids + tables_booked_ids_temp

    # Then I get a list of all the tables, of the needed size, available in that restaurant and
    # I exclude the previous list of unavailable tables. I order the list from the smaller table
    # to the bigger one and I return the first, smaller one, available.
    tables = Table.objects.all().filter(status="Non",size__gte=people).exclude(id__in=tables_booked_ids).order_by('size')
    for value in tables:
        print(value.size)

    print(tables.count())
    """
    tables_booked = Table.objects.all()
    for value in tables_booked:
        print(value.status)
    tables = Table.objects.filter(restaurant=restaurant,
        restaurant__opening_time__lte=booking_date_time.hour,
        restaurant__closing_time__gte=booking_date_time.hour
                                      +(minutes_slot / float(60)),
        size__gte=people).exclude(id__in=tables_booked_ids).order_by('size')
    print(tables)"""
    if tables.count() == 0:
        return None
    else:
        return tables[0]

def get_expected_diners(restaurant, booking_date):
    """
    Return the expected number of diners of a restaurant for a specific date.
    """
    diners = Booking.objects.filter(
        table__restaurant=restaurant,
        booking_date_time_start__year=booking_date.year,
        booking_date_time_start__month=booking_date.month,
        booking_date_time_start__day=booking_date.day).aggregate(Sum('people'))
    return diners['people__sum']

# Create your views here.

from .forms import RestaurantForm,BookingForm,TableForm
def Outtime(request):
    #form_class=RestaurantForm

    #form_class = BookingForm
    #form=form_class(request.POST)
    #if request.method=="POST":
    if request.POST:
        #form = OrderForm(request.POST)

        # form1 = RestaurantForm(request.POST)


        form2 = BookingForm(request.POST)
        form3 = TableForm(request.POST)
        if form2.is_valid():
            if form3.is_valid():
                document_item2 = form2.save(commit=False)
                document_item3 = form3.save(commit=False)
                # Outtime = request.POST.get('Outtime')
                # status1 = request.POST.get('status1')
                # status2 = request.POST.get('status2')
                # document_item1.save()
                document_item2.save()
                document_item3.save()
                restaurant = request.POST.get('restaurant')
                print("rest", restaurant)
                booking_date_time_start = request.POST.get('booking_date_time_start')
                print(booking_date_time_start)
                booking_date_time_end = request.POST.get('booking_date_time_end')
                people = request.POST.get('people')
                c=book_restaurant_table(restaurant, booking_date_time_start, people)
                print(c)
                #return render(request,'/Booking', messages.success(request, 'Booking was successfully created.', 'alert-success'))
                #return render(request, 'index1.html', {'booking': booking.id, 'table': table.id})
                return render(request, 'index1.html', {'c': c})

            #   document_item1 = form1.save(commit=False)

    else:
        #form1=RestaurantForm()
        form2 = BookingForm()
        form3 = TableForm()
        return render(request, 'Booking.html', { 'form2': form2,'form3':form3})

#    return render(request,'restaurants/Booking.html',{'form1':form1,'form2':form2,'form3':form3})

def AvailableTable(request):
    get=Table.objects.all().filter(status="Non")
    print(get.count())
    tables_booked = Table.objects.all()
    for value in tables_booked:
        print(value.status)
#status = request.POST.get('status')


def book(request):
    if request.POST:
        form2 = BookingForm(request.POST)
        form3 = TableForm(request.POST)
        if form2.is_valid():
            if form3.is_valid():
                restaurant = request.POST.get('restaurant')
                print("rest", restaurant)
                booking_date_time_start = request.POST.get('booking_date_time_start')
                print(booking_date_time_start)
                booking_date_time_end = request.POST.get('booking_date_time_end')
                people = request.POST.get('people')
                c=book_restaurant_table(restaurant, booking_date_time_start, people)
                print(c)
                return render(request, 'index1.html', {'c': c})

            #   document_item1 = form1.save(commit=False)

    else:
        #form1=RestaurantForm()
        form2 = BookingForm()
        form3 = TableForm()
        return render(request, 'Booking.html', { 'form2': form2,'form3':form3})



def all_booking(request):
    booking = Booking.objects.all()
    print(booking)
    return render(request, 'all_booking.html', {'booking': booking})




def order(request):

    #return render(request, 'Menu.html', {'products': products, 'item1': item1})
    form = OrderForm(request.POST)
    products = Product.objects.all()
    item1 = Product.objects.values_list('type', flat=True).distinct()
    #print(item1)
    #print(products)
    if request.POST:


        print (form.errors)
        if form.is_valid():
            people = request.POST.getlist('item')
            #people = request.POST.getlist
            print(people)
            quantitylist = request.POST.getlist('quantity')
            print(quantitylist)
            quantitylist=list(filter(lambda a: a != '0', quantitylist))
            ans=0
            for value,quantity in zip(people,quantitylist):
                print(value)
                rate=Product.objects.get(product_name=value)
                print(rate.price)
                ans=ans+(rate.price*int(quantity))
            print(quantitylist)
            print(ans)
            if form.save():
                # return render(request, 'New.html', {'products': products, 'item1': item1})

                return redirect('/', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))



        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'order.html', {'form':form,'products': products, 'item1': item1})


from django.shortcuts import render,redirect,HttpResponse,render_to_response,get_object_or_404

import pandas as pd
from django.http import HttpResponseRedirect
from django.urls import resolvers
#from django.core.urlresolvers import reverse
# Create your views here.


def index2(request):
    return render(request, 'index2.html')


def onday(request):

    if request.method == 'POST':
        day=request.POST.get('handle')
    #reading csv file
    readfile = pd.read_csv("C:\\Users\\SAI\\PycharmProjects\\MyRestaurant\\User.csv")
    #groupby on column day
    user_grp = readfile.groupby(['day'])
    unique_date = user_grp.date.unique()
    Key_value = unique_date.index.values
    list_day = list(Key_value)
    total = user_grp.date.count()
    for i in range(6):
        if list_day[i].lower() == day.lower():
            no_of_users=int(total[i] / len(unique_date[i]))
            context={
                'day':day,

                'ans': no_of_users
            }
            print(total[i] / len(unique_date[i]))
    return render(request, 'Prediction.html',context)
##################################################################################################
#from .forms import DateForm
#from .models import ClassModel
from django import forms

def detail1(request):
    if request.method == 'POST':
        day1 = request.POST.get('ganu')
        month,day,year=(int(x) for x in day1.split('-'))
        ans=datetime.date(month,day,year)
        day=ans.strftime("%A")
        print("date_time_obj")
        print(day)
        readfile = pd.read_csv("C:\\Users\\SAI\\PycharmProjects\\MyRestaurant\\User.csv")
        user_grp = readfile.groupby(['day'])
        unique_date = user_grp.date.unique()
        Key_value = unique_date.index.values
        list_day = list(Key_value)
        total = user_grp.date.count()
        for i in range(6):
            if list_day[i].lower() == day.lower():
                no_of_users=int(total[i] / len(unique_date[i]))
                context={
                    'day':day,

                    'ans': no_of_users
                    }
                print(total[i] / len(unique_date[i]))
    return render(request, 'Prediction.html',context)


def order1(request):

    #return render(request, 'Menu.html', {'products': products, 'item1': item1})
    form = OrderForm(request.POST)
    products = Product.objects.all()
    item1 = Product.objects.values_list('type', flat=True).distinct()
    #print(item1)

    #print(products)
    if request.POST:


        print (form.errors)
        if form.is_valid():
            people = request.POST.getlist('item')
            people1 = request.POST.getlist('product_id')
            #people = request.POST.getlist
            print(people)
            print(people1)
            quantitylist = request.POST.getlist('quantity')
            print(quantitylist)
            quantitylist=list(filter(lambda a: a != '0', quantitylist))
            ans=0
            for value,quantity in zip(people,quantitylist):
                print(value)
                rate=Product.objects.get(product_name=value)
                print(rate.price)
                ans=ans+(rate.price*int(quantity))
            print(quantitylist)
            print("Bill",ans)
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save_m2m()
            if form.save():
                # return render(request, 'New.html', {'products': products, 'item1': item1})

                return redirect('/', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))



        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'order1.html', {'form':form,'products': products, 'item1': item1})



