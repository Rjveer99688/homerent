from django import forms
from .models import *


class MeterReadingForm(forms.ModelForm):
  class Meta:
    model = MeterReading
    fields = ["unit"]
    labels = {"unit":"Meter Reading"}

class AmtPaidForm(forms.ModelForm):
  class Meta:
    model = PaymentDetail
    fields=["paidamount"]
    labels={"paidamount":"Amount Paid"}
