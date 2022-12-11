from django.http import HttpResponse
from django import forms
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages



# Create your views here.
def homepage(request):
    return HttpResponse("welcome")

def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
        object = form.save(commit=False)
        object.username = request.user.username
        object.save()
        form = MyForm()
        messages.success(request, 'Submitted successfully.')
        
  else:
      form = MyForm()
      messages.error(request, 'Invalid form submission.')

  return render(request, 'homepage.html', {'form': form})

def my_form1(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    form1 = Transactions(request.POST)
    if form.is_valid():
        object = form.save(commit=False)
        object.username = request.user.username
        object.save()

        tusername=request.user.username
        tlast_unit=Profile.objects.values_list('last_unit', flat=True).filter(username=tusername)[0]
        tnew_unit=object.electricunit
        tunit_consumed=tnew_unit-tlast_unit
        tebill_amt=tunit_consumed*7
        ttotal_amount=tebill_amt+1000+Profile.objects.values_list('balance', flat=True).filter(username=tusername)[0]
        tamount_paid=object.paidamount
        tbalance=ttotal_amount-tamount_paid

        transactions = Transactions.objects.create(username=tusername,last_unit=tlast_unit,new_unit=tnew_unit,unit_consumed=tunit_consumed,ebill_amt=tebill_amt,total_amount=ttotal_amount,amount_paid=tamount_paid,balance=tbalance)
        profiles = Profile.objects.all().filter(username=tusername).update(last_unit=tlast_unit,balance=tbalance)
        transactions.save()
        #profiles.save()

        form = MyForm()
        messages.success(request, 'Submitted successfully.')
        
  else:
      form = MyForm()
      messages.error(request, 'Invalid form submission.')

  return render(request, 'homepage.html', {'form': form})

