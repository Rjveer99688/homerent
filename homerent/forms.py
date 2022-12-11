from django import forms
from .models import *

class MyForm(forms.ModelForm):
  class Meta:
    model = UsersDetails
    fields=["electricunit","paidamount"]
    labels={"electricunit":"E-unit","paidamount":"Paid-Amount"}


class ProfileForm(forms.ModelForm):
  class Meta:
    model=Profile
    fields=["username","home_no","building","room_no","last_unit","tarrif","balance"]#,"balance_last_updated_at","created_at","updated_at"]
    labels={"username":"Username","home_no":"Home_no","building":"Building","room_no":"Room_no","last_unit":"Last_unit","tarrif":"Tarrif","balance":"Balance","balance_last_updated_at":"Balance_last_updated_at","created_at":"Created At","updated_at":"Updated By"}#"created_at","updated_at"]
    
class TransactionsForm(forms.ModelForm):
  class Meta:
    model=Transactions
    fields=["username","last_unit","new_unit","unit_consumed","ebill_amt","total_amount","amount_paid","balance"]#,"created_at","updated_at"]
    labels={"username":"Username","last_unit":"Last_unit","new_unit":"New_unit","unit_consumed":"Unit_consumed","ebill_amt":"Ebill_amt","total_amount":"Total_amount","amount_paid":"Amount_paid","balance":"Balance","created_at":"Created At","updated_at":"Updated By"}
    
