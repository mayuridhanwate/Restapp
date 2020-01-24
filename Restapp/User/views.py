
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from .models import Customer
from Tag.models import Foody
from Feedback.models import Response
from .forms import CustomerForm,OutForm,ResponseForm,FoodyForm
import datetime
from datetime import datetime
import datetime

def index(request):
    form_class=CustomerForm
    form=form_class(request.POST)
    if request.method=="POST":
        form=CustomerForm(request.POST)

        if form.is_valid():
            document_item = form.save(commit=False)
            document_item.save()
    else:
        form=CustomerForm()
    return render(request,'Userform.html',{'form':form})



def validate_Mobile_No(request):
    Mobile_No = request.GET.get('Mobile_No')
    d = Customer.objects.raw('SELECT * FROM User_customer WHERE Mobile_No=Mobile_No ')[0]
    name=d.Name
    add=d.Address
    currentDT = datetime.datetime.now()

    date=currentDT.strftime("%Y-%m-%d")
    i=currentDT.strftime("%I:%M:%S")
    day=currentDT.strftime("%A")

    if d:
        data = {
            'is_taken': Customer.objects.filter(Mobile_No__iexact=Mobile_No).exists(),
            'name': name,
            'add': add,
            'i': i,
            'o': i,
            'date': date,
            'day': day,
        }
    else:
        currentDT = datetime.datetime.now()
        date = currentDT.strftime("%Y-%m-%d")
        i = currentDT.strftime("%I:%M:%S %p")
        day = currentDT.strftime("%A")
        data={
            'is_taken': Customer.objects.filter(Mobile_No__iexact=Mobile_No).exists(),
            'i': i,
            'o': i,
            'date': date,
            'day': day,
        }
    return JsonResponse(data)
"""
def Outtime(request):
    form_class=OutForm
    form=form_class(request.POST)
    if request.method=="POST":

        form1 = OutForm(request.POST)


        form2 = ResponseForm(request.POST)
        form3 = FoodyForm(request.POST)
        if form.is_valid():
            Mobile_No = request.GET.get('Mobile_No')
            Outtime = request.POST.get('Outtime')
            status1 = request.POST.get('status1')
            status2 = request.POST.get('status2')
            print(Outtime)
            e = Customer.objects.filter(Mobile_No=Mobile_No, Status='Active').update(Outtime='Outtime',Status='Inctive')

            m = e.pk
            print(m)
            document_item1 = form1.save(commit=False)
            document_item2 = form2.save(commit=False)
            document_item3 = form3.save(commit=False)
            Outtime = request.POST.get('Outtime')
            status1 = request.POST.get('status1')
            status2 = request.POST.get('status2')
            document_item1.save()
            document_item2.save()
            document_item3.save()
    else:
        form1=OutForm()
        form2 = ResponseForm()
        form3 = FoodyForm()
    return render(request,'Outtime.html',{'form1':form1,'form2':form2,'form3':form3})

def savedata(request):
    Mobile_No = request.GET.get('Mobile_No')
    if request.method == 'POST':
        form = OutForm(request.POST)
        if form.is_valid():
            #Outtime = request.POST.get('Outtime')
            #status1 = request.POST.get('status1')
            #status2 = request.POST.get('status2')
            #print(Outtime)
            
            import pandas as pd
            import sqlite3
            con = sqlite3.connect('C:\\Users\\SAI\\PycharmProjects\\Project1\\db.sqlite3')
            df = pd.read_sql_query('SELECT * from User_customer', con)

            print(df)
            cur = con.cursor()
            cur.execute("update User_customer set Outtime=Outtime where Mobile_No=Mobile_No and Status='Active'")
            con.commit()
            df1 = pd.read_sql_query('SELECT * from User_customer', con)
            #e = User_customer.objects.filter(Mobile_No=Mobile_No, Status='Active').update(Outtime='Outtime',
             #                                                                             Status='Inctive')

            #print(df1)

            print(Outtime)
            #e=Customer.objects.filter(Mobile_No=Mobile_No ,Status='Active').update(Outtime=Outtime,Status='Inctive')
            #print(e)

            #e=Customer.objects.raw('SELECT * FROM User_customer WHERE Mobile_No=Mobile_No AND Status="Active"')
            #e.update(Outtime=Outtime,Status='Inctive')
            #m=e.pk
            #print(m)
            #e.Outtime=Outtime
            #e.save()
            #obj1=Response(status1=status1,f_key=m)
            #obj1.save()
            #obj2=Foody(status2=status2, f_key=m)
            #obj2.save()
            # request.session['Value'] = {Mobile_No,Name,Address,Intime,Date,Day,Pax}
            #request.session['Value'] = context
            #print(request.session['Value'])
            #return redirect(request,'Restaurant/')
            #return HttpResponseRedirect(reverse('Restaurant/'))
    #return redirect(reversed('Restaurant/index'))
    return redirect('/Restaurant/Outtime')

"""
def Outtime(request):
    if request.POST:
        form1 = FoodyForm(request.POST)
        form2 = OutForm(request.POST)
        form3 = ResponseForm(request.POST)
        if form2.is_valid():
            if form3.is_valid():
                Mobile_No = request.POST.get('Mobile_No')
                print(Mobile_No)
                Outtime = request.POST.get('Outtime')
                print(Outtime)
                status1 = request.POST.get('status1')
                status2 = request.POST.get('status2')
                #print(Outtime)
                m=Customer.objects.filter(Mobile_No=Mobile_No,Status='Active')

                print(m)
                for obj in m:
                    obj.Outtime=Outtime
                    obj.Status='Inactive'
                    obj.save()
                    m=obj.pk
                    robj = Response(status1=status1, f_key=obj)
                    robj.save()
                    fobj=Foody(status2=status2,f_key=obj)
                    fobj.save()
                    """
                    fobj = Foody.objects.filter(f_key=m)
                    for f in fobj:
                        f.status2=status2
                        
                    robj = Response.objects.filter(f_key=m)
                    for r in robj:
                        r.status2 = status2
"""
                    print("ID",m)


            return render(request, 'Outtime.html')

    else:
        form1=OutForm()
        form2 = ResponseForm()
        form3 = FoodyForm()
        return render(request,'Outtime.html',{'form1':form1,'form2':form2,'form3':form3})
