from django.db import models
from django.db.models.signals import post_save, post_init

class UsersDetails(models.Model):
    username=models.CharField(max_length=200)
    electricunit=models.IntegerField(max_length=7)
    paidamount=models.IntegerField(max_length=50)
    verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username+str(self.created_at) 

    @staticmethod
    def verifieds(sender, instance, created, **kwargs):
        print("unside verified")
        if instance.verified: #paidamount==1000:# is True: #!= instance.state or created:
            #instance.paidamount=instance.paidamount+1
            print("unside verified"+str(instance.paidamount))
            #instance.save()
            #do_something_with_state_change()  
            execute_transaction(instance)

post_save.connect(UsersDetails.verifieds, sender=UsersDetails)

class Profile(models.Model):
    username=models.CharField(max_length=200)
    home_no = models.CharField(max_length=10)
    building=models.CharField(max_length=200)
    room_no=models.IntegerField(max_length=7)
    last_unit=models.IntegerField(max_length=7)
    tarrif = models.IntegerField(max_length=7)
    balance  = models.IntegerField(max_length=7)
    balance_last_updated_at = models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Transactions(models.Model):    
    username=models.CharField(max_length=200)    
    last_unit=models.IntegerField(max_length=7)
    new_unit=models.IntegerField(max_length=7)
    unit_consumed = models.IntegerField(max_length=7)
    ebill_amt = models.IntegerField(max_length=7)
    total_amount = models.IntegerField(max_length=7)
    amount_paid = models.IntegerField(max_length=7)
    balance = models.IntegerField(max_length=7)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username+str(self.created_at) 

    
def execute_transaction(instance):
    tusername=instance.username
    tlast_unit=Profile.objects.values_list('last_unit', flat=True).filter(username=tusername)[0]
    tnew_unit=instance.electricunit
    tunit_consumed=tnew_unit-tlast_unit
    tebill_amt=tunit_consumed*7
    ttotal_amount=tebill_amt+1000+Profile.objects.values_list('balance', flat=True).filter(username=tusername)[0]
    tamount_paid=instance.paidamount
    tbalance=ttotal_amount-tamount_paid

    transactions = Transactions.objects.create(username=tusername,last_unit=tlast_unit,new_unit=tnew_unit,unit_consumed=tunit_consumed,ebill_amt=tebill_amt,total_amount=ttotal_amount,amount_paid=tamount_paid,balance=tbalance)
    profiles = Profile.objects.all().filter(username=tusername).update(last_unit=tlast_unit,balance=tbalance)
    transactions.save()    









