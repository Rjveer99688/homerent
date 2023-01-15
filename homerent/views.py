from django.http import HttpResponse
from django import forms
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.utils.timezone import now
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import login_required


# Create your views here.
def get_referer(request):
  referer = request.META.get('HTTP_REFERER')
  if not referer:
    return None
  return referer

@login_required(login_url='/accounts/login/')
def home(request):
  print("inside home")
  submitUnit=False
  makePayment=False
  currentDate = datetime.now().date()
  startDate = currentDate.replace(day=1)
  endDate = currentDate.replace(day=10)
  print (currentDate,startDate,endDate)

  profile = Profile.objects.all().filter(username=request.user.username)[0]
  transaction = Transaction.objects.filter(username=request.user.username).values('payment_id__created_at','bill_id__new_unit','total_amount', 'amount_paid', 'balance').order_by('-payment_id__created_at')[:5]
  lastPayment = "none"
  
  # For Unit Submission link
  lastSubmitDate=MeterReading.objects.values_list('created_at', flat=True).filter(username=request.user.username).order_by('-created_at')[0]
  if(startDate <= currentDate <= endDate) and (lastSubmitDate<startDate):
    submitUnit=True

  # For Payment Link
  lastBill=Bill.objects.all().filter(username=request.user.username).order_by('-created_at')[0]
  print(startDate,lastBill.created_at.date(), startDate+relativedelta(months=1))
  if(startDate<=lastBill.created_at.date()<(startDate+relativedelta(months=1))) and (lastBill.paid==False):
    makePayment=True
  else:
    lastPayment = PaymentDetail.objects.filter(username=request.user.username,verified=False).values('created_at','bill_id__new_unit','bill_id__total_amount', 'paidamount' ).order_by('-created_at')[:1]
    
  context={
    'submitUnit':submitUnit,
    'makePayment':makePayment,
    'profile':profile,
    'transaction':transaction,
    'lastPayment':lastPayment
  }
  return render(request, 'home.html',context)


def eunit(request):
  if not get_referer(request):
    return redirect('/home')

  if request.method == "POST":
    form = MeterReadingForm(request.POST)
    if form.is_valid():
      object = form.save(commit=False)
      lastUnit=Profile.objects.values_list('last_unit', flat=True).filter(username=request.user.username)[0]
      if(lastUnit<object.unit):
        object = form.save(commit=False)
        object.username = request.user.username
        object.save()
        form = MeterReadingForm()
        messages.success(request, 'Submitted successfully.')
      else:
        messages.warning(request, 'Incorrect Meter Reading Entered .')
        
  else:
      form = MeterReadingForm()

  context = {
        'MeterReading': form,
    }

  return render(request, 'eunit.html', context=context)


def payment(request):
  if not get_referer(request):
    return redirect('/home')
    
  bill=Bill.objects.all().filter(username=request.user.username).order_by('-created_at')[0]
  if request.method == "POST":
    form = AmtPaidForm(request.POST)
    if form.is_valid():
      object = form.save(commit=False)
      object.username = request.user.username
      object.bill_id = Bill.objects.all().filter(id=bill.id)[0]
      object.save()
      form = AmtPaidForm()
      bill = Bill.objects.all().filter(id=bill.id).update(paid=True)

      messages.success(request, 'Submitted successfully.')
    else:
      messages.success(request, 'Incorrect payment info entered .')
        
  else:
      form = AmtPaidForm()

  context = {
        'bill': bill,
        'AmtPaidForm': form
    }
  return render(request,'payment.html',context=context)

