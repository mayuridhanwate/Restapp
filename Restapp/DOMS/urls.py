"""DOMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from orders import views as my_order
from User import views as userview
from django.contrib.auth import views as auth
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', my_order.index, name='home'),
    url(r'^orders$', my_order.index, name='home'),
    url(r'^order/(?P<order_id>\d+)/$', my_order.show, name='show'),
    url(r'^order/new/$', my_order.new, name='new'),
    url(r'^order/edit/(?P<order_id>\d+)/$', my_order.edit, name='edit'),
    url(r'^order/delete/(?P<order_id>\d+)/$', my_order.destroy, name='delete'),
    url(r'^products$', my_order.index_product, name='home_product'),
    url(r'^product/new/$', my_order.new_product, name='new_product'),
    url(r'^product/delete/(?P<product_id>\d+)/$', my_order.destroy_product, name='delete_product'),
    url(r'^AllMenu$', my_order.AllMenu, name='AllMenu'),
    #url(r'^users/login/$', my_order.LoginView.as_view(template_name=login.html), name='login'),
    #url(r'^users/login/$', my_order.login, {'template_name': 'login.html'}, name='login'),
    #url( r'^login/$',my_order.LoginView.as_view(template_name="login.html"), name="login"),
    path('users/login', LoginView.as_view(), name='login'),
    path('users/logout', LogoutView.as_view(), name='logout'),
    path(r'Restaurant/', include('orders.urls')),
    url(r'^all_booking$', my_order.all_booking, name='all_booking'),
    url(r'^book$', my_order.book, name='book'),
    url(r'^neworder$', my_order.order, name='neworder'),
    url(r'^neworder1$', my_order.order1, name='neworder1'),
    path(r'Userform/', include('User.urls')),

    #url(r'^users/logout/$', auth.logout, {'next_page': '/'}, name='logout'),
   # url(r'^users/change_password/$', login_required(auth.password_change), {'post_change_redirect' : '/','template_name': 'change_password.html'}, name='change_password'),
    path(r'Booking/', my_order.index1, name='index1'),
]
