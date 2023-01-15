from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PaymentDetail)
admin.site.register(Profile)
admin.site.register(Transaction)
admin.site.register(MeterReading)
admin.site.register(Bill)


