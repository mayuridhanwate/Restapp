from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from . import views
app_name = 'orders'

urlpatterns = [
    #path('', views.Outtime, name='Outtime'),
    path('', views.index, name='index'),
    url(r'detail/$', views.detail1, name='detail1'),
    url(r'onday/$', views.onday, name='onday'),

    #path(r'Booking/', views.index1, name='index1'),
    #path(r'Booking/Detail', views.index, name='index'),
    #path(r'Available/', views.AvailableTable, name='AvailableTable'),

]