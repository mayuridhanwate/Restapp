#from .models import Customer,Restaurant,Menu
from .models import Customer
from django.forms import ModelForm
from Feedback.models import Response
from Tag.models import Foody


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['Mobile_No', 'Address', 'Name', 'Intime',  'Date', 'Day', 'Pax','Status']



class OutForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['Mobile_No','Outtime']

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = [ 'status1']

class FoodyForm(ModelForm):
    class Meta:
        model = Foody
        fields = [ 'status2']


