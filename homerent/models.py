from django.db import models
from django.db.models.signals import post_save, post_init


def gen_bill(instance):
    print('inside get_bill')
    tusername=instance.username
    tlast_unit=Profile.objects.values_list('last_unit', flat=True).filter(username=tusername)[0]
    tnew_unit=instance.unit
    ttariff=Profile.objects.values_list('tarrif', flat=True).filter(username=tusername)[0]
    tunit_consumed=tnew_unit-tlast_unit
    tebill_amt=tunit_consumed*ttariff
    tbalance=Profile.objects.values_list('balance', flat=True).filter(username=tusername)[0]
    trent=Profile.objects.values_list('room_rent', flat=True).filter(username=tusername)[0]
    ttotal_amount=tebill_amt+trent+tbalance

    bill = Bill.objects.create(username=tusername,
    last_unit=tlast_unit,
    new_unit=tnew_unit,
    tariff=ttariff, 
    unit_consumed=tunit_consumed,
    ebill_amt=tebill_amt,
    rent=trent, 
    balance=tbalance,
    fine=0,
    total_amount=ttotal_amount)
    bill.save()
    Profile.objects.all().filter(username=tusername).update(last_unit=tlast_unit,balance=ttotal_amount)


class MeterReading(models.Model):
    username=models.CharField(max_length=200)
    unit=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.username+str(self.created_at)     

    @staticmethod
    def generateBill(sender, instance, created, **kwargs):
        print("inside generateBill")
        gen_bill(instance)
    
post_save.connect(MeterReading.generateBill, sender=MeterReading)   


class Bill(models.Model):
    username=models.CharField(max_length=200)
    last_unit=models.IntegerField()
    new_unit=models.IntegerField()
    tariff=models.DecimalField(max_digits=8,decimal_places=3)
    unit_consumed = models.IntegerField()
    ebill_amt = models.DecimalField(max_digits=8,decimal_places=3)
    rent = models.IntegerField()
    balance = models.DecimalField(max_digits=8,decimal_places=3)
    fine = models.DecimalField(max_digits=8,decimal_places=3)
    total_amount = models.DecimalField(max_digits=8,decimal_places=3)
    paid=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username+str(self.created_at) 


class PaymentDetail(models.Model):
    username=models.CharField(max_length=200)
    bill_id=models.ForeignKey(Bill, null=False, on_delete=models.CASCADE)
    paidamount=models.IntegerField()
    verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username+str(self.created_at) 

    @staticmethod
    def verifieds(sender, instance, created, **kwargs):
        print("inside verified")
        print("instance",instance,instance.id)
        if instance.verified:
            print("unside verified"+str(instance.paidamount))
            execute_transaction(instance)
    
post_save.connect(PaymentDetail.verifieds, sender=PaymentDetail)

class Transaction(models.Model):    
    username=models.CharField(max_length=200)
    bill_id=models.ForeignKey(Bill, null=False, on_delete=models.CASCADE)
    payment_id=models.ForeignKey(PaymentDetail, null=False, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    amount_paid = models.IntegerField()
    balance = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username+str(self.created_at) 


class Profile(models.Model):
    username=models.CharField(max_length=200)
    full_name=models.CharField(max_length=200)
    contact_no=models.BigIntegerField()
    door_no = models.CharField(max_length=10)
    building_no=models.IntegerField()
    building_name=models.CharField(max_length=200)
    room_rent=models.IntegerField()
    last_unit=models.IntegerField()
    tarrif = models.DecimalField(max_digits=8,decimal_places=3)
    balance  = models.DecimalField(max_digits=8,decimal_places=3)
    last_transaction_id = models.ForeignKey(Transaction, null=True, on_delete=models.CASCADE)
    balance_last_updated_at = models.DateTimeField(auto_now=True)


    image = models.ImageField(default='default.png', upload_to='profile_pics')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    
def execute_transaction(instance):
    tusername=instance.username
    tbill_id=instance.bill_id
    tpayment_id=instance
    ttotal_amount=instance.bill_id.total_amount 
    tbalance=ttotal_amount-tamount_paid

    transactions = Transaction.objects.create(username=tusername,bill_id=tbill_id,payment_id=tpayment_id,total_amount=ttotal_amount,amount_paid=tamount_paid,balance=tbalance)
    profiles = Profile.objects.all().filter(username=tusername).update(last_unit=instance.bill_id.new_unit,balance=tbalance,last_transaction_id=transactions)
    transactions.save()    









