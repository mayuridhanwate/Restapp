from django.urls import path, include
from django.conf.urls import url
from . import views
# from User.models import Food
from django.conf.urls import url
from django.views.generic import ListView
# from User.models import Food
from django.conf import settings

app_name = 'User'

urlpatterns = [
    url(r'validate_Mobile_No/$', views.validate_Mobile_No, name='validate_Mobile_No'),
    # path('', views.customer_list, name='customer_list'),
    path('', views.index, name='index'),
    path(r'Outtime/', views.Outtime, name='Outtime'),

    #path(r'^signup/$',views.SignUpView.as_view(),name='signup'),
     #url(r'validate_Mobile_No/$', views.validate_Mobile_No, name='validate_Mobile_No'), #   path('', views.customer_list, name='customer_list'),
]