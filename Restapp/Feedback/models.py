
from django.db import models
from User.models import Customer
# Create your models here.
class Response(models.Model):
    choice=(('H','happy'),('Un','unhappy'))
    status1 = models.CharField(max_length=50,blank=True,choices=choice)
    f_key = models.ForeignKey(Customer,on_delete='models.CASCADE',null=True)

    def __str__(self):  # __unicode__ on Python 2
        return '%s' % self.status1