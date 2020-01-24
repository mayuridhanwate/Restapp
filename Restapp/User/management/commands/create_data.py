import os
from faker import Faker
import csv
from datetime import time,datetime,timedelta
import datetime

record_count=100
import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
fake=Faker()
os.environ['DJANGO_SETTINGS_MODULE'] = 'Project.settings'
os.environ.setdefault('DJANGO_SETTINGS_VALUE','Project.settings')

import django
django.setup()

from User.models import Customer
from Feedback.models import Response
from Tag.models import Foody
class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            start_date = datetime.date(year=2015, month=1, day=1)
            end_date = datetime.date(year=2016, month=1, day=1)

            date = fake.date_between(start_date=start_date, end_date=end_date)
            day = date.strftime("%A")
            it = fake.time()
            hour, minute, second = (int(x) for x in it.split(':'))
            # import datetime
            #select_choice1=["happy","unhappy"]
            select_choice1 = [('H','happy'),('Un','unhappy')]
           # select_choice2 = ["Vegeterian", "Non_Vegeterian"]
            select_choice2 = [('V','Vegeterian'),('Non','Non_Vegeterian')]

            c1=random.choice(select_choice1)
            c2 = random.choice(select_choice2)
            d1 = datetime.datetime(2000, 1, 1, hour, minute, second)
            #print(c1)
            a = random.randint(1, 10)

            if a == 1:
                d2 = d1 + timedelta(minutes=15)
            elif a >= 2 and a <= 5:
                d2 = d1 + timedelta(minutes=35)
            else:
                d2 = d1 + timedelta(hours=1, minutes=5)
            foo_instance = Customer.objects.create(Name=fake.name(), Address=fake.address(),
                                                   Mobile_No=fake.phone_number(),
                                                   Intime=it,
                                                   Outtime=d2.time(),
                                                   Date=date,
                                                   Day=day,
                                                   Pax=a, )

            foo_instance.save()

            foo1_instance = Response.objects.create(status1=c1,
                                                   f_key=foo_instance,
                                                   )
            foo1_instance.save()
            foo2_instance = Foody.objects.create(status2=c2,
                                                    f_key=foo_instance,
                                                    )
            foo2_instance.save()
