from django.db import models
from django.conf import settings
from datetime import date
from django.contrib import admin
from django.dispatch import receiver
from django.db.models.signals import post_save
from app.sms import Sms
import schedule
import time
import datetime

# Create your models here.

class User(models.Model):

    ACTIVE = 'Active'
    PENDING = 'Pending'
    DORMANT = 'Dormant'
    BLOCKED = 'Blocked'
    STATUS = (
        (ACTIVE, 'Active'),
        (PENDING, 'Pending'),
        (DORMANT, 'Dormant'),
        (BLOCKED, 'Blocked'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_id = models.CharField(unique=True,max_length=8,default=12345678)
    phone_no = models.CharField(unique=True,max_length=15,default='0712345678')
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=15,choices=STATUS,default=PENDING)
    loan_limit = models.FloatField(default=200.00)
    residence = models.CharField(max_length=100)
    device_id = models.BigIntegerField(blank=True,default=0)


class Loan(models.Model):
    ACTIVE  = 'Active'
    PENDING = 'Pending'
    SETTLED = 'Settled'
    BLOCKED = 'Blocked'
    STATUS  = (
        (ACTIVE, 'Active'),
        (PENDING, 'Pending'),
        (SETTLED, 'Settled'),
        (BLOCKED, 'Blocked'),
    )

    user = models.ForeignKey(
	    User,
	    verbose_name="Loan Applicant",
    )
    applicationDate = models.DateField()
    dueDate = models.DateField()
    loan_amount = models.FloatField(default=0.00)
    loan_balance = models.FloatField(default=0.00)
    status = models.CharField(max_length=15,choices=STATUS,default=PENDING)


class Settlement(models.Model):
    OK  = 'Ok'
    PENDING = 'Pending'
    FAILED = 'Failed'
   
    STATUS  = (
        (OK, 'Ok'),
        (PENDING, 'Pending'),
        (FAILED, 'Failed'),
    )

    loan = models.ForeignKey(
	    Loan,
	    on_delete=models.CASCADE,
	    verbose_name="Loan",
    )
    date = models.DateField()
    amount = models.FloatField(default=0.00)
    reference = models.CharField(max_length=20)
    status = models.CharField(max_length=15,choices=STATUS,default=PENDING)

class Statement(models.Model):
    user = models.ForeignKey(
	    User,
	    verbose_name="Loan Applicant",
    )
    details = models.CharField(max_length=500)

class Activation(models.Model):
    user = models.ForeignKey(
	    User,
	    verbose_name="Loan Applicant",
    )

    OK  = 'Ok'
    PENDING = 'Pending'
    FAILED = 'Failed'
   
    STATUS  = (
        (OK, 'Ok'),
        (PENDING, 'Pending'),
        (FAILED, 'Failed'),
    )

    reference = models.CharField(max_length=500)
    status = models.CharField(max_length=15,choices=STATUS,default=PENDING)

#signals

@receiver(post_save, sender=Activation)
def check_activation_status(sender, instance, created, **kwargs):
    activation = instance
    if activation.status=="Ok":
        user = User.objects.get(pk=activation.user.id)
        user.status = "Active"
        message = "KOPESHA LOANS \n Dear "+user.first_name+",Your Account is now active.You can now start borrowing loans."
        to = "+254"+user.phone_no
        Sms.send_message(to,message)

        user.save()
    elif activation.status == "Pending" or activation.status == "Failed":
        user = User.objects.get(pk=activation.user.id)
        if user.status == "Active":
            user.status = "Pending"
            user.save()

@receiver(post_save, sender=Settlement)
def check_settlement_status(sender, instance, created, **kwargs):
    settlement = instance
    if(settlement.status=="Ok"):
        loan = Loan.objects.get(pk=settlement.loan.id)
        loan.loan_balance = loan.loan_balance - settlement.amount
        if loan.loan_balance == 0 or loan.loan_balance<0:
            loan.status = "Settled"
            user = User.objects.get(pk=loan.user.id)
            user.loan_limit = user.loan_limit * 1.2
            user.save()
        loan.save()

    elif settlement.status == "Pending" or settlement.status == "Failed":
        loan = Loan.objects.get(pk=settlement.loan.id)
        if loan.status == "Active":
            loan.loan_balance = loan.loan_balance + settlement.amount
        if loan.loan_balance == 0 or loan.loan_balance<0:
            loan.status = "Settled"
        loan.save()


    
def send_reminders():
    two_days_from_now = get_date('%Y-%m-%d',2)
    today = get_date('%Y-%m-%d',0)
    loans = Loan.objects.all()
    for loan in loans:
        if loan.due_date == two_days_from_now:
             user = User.objects.get(pk=loan.user.id)
             message = "KOPESHA LOANS \n Dear "+user.first_name+",Your Loan of Ksh."+loan.loan_amount+" is due on "+loan.due_date+".Please pay your balance of Ksh."+loan.loan_balance
             to = "+254"+user.phone_no
             Sms.send_message(to,message)

        elif loan.due_date == today:
             user = User.objects.get(pk=loan.user.id)
             message = "KOPESHA LOANS \n Dear "+user.first_name+",Your Loan of Ksh."+loan.loan_amount+" is due today.Please pay your balance of Ksh."+loan.loan_balance+" to avoid blacklisting"
             to = "+254"+user.phone_no
             Sms.send_message(to,message)


def get_date(dateFormat="%Y-%m-%d", addDays=0):

    timeNow = datetime.datetime.now()
    if (addDays!=0):
        anotherTime = timeNow + datetime.timedelta(days=addDays)
    else:
        anotherTime = timeNow

    return anotherTime.strftime(dateFormat)      


schedule.every().day.at("10:00").do(send_reminders)
while True:
    schedule.run_pending()
    time.sleep(1)





  






	



