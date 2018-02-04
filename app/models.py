from django.db import models
from django.conf import settings
from django.contrib import admin
from django.dispatch import receiver
from django.db.models.signals import post_save
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)
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
        user.save()
        message = "KOPESHA LOANS \nDear "+user.first_name+",Your Kopesha Account is now active.You can now get a loan."
        to = "+254"+user.phone_no
        send_message(to,message)
        
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
        if loan.loan_balance == 0 or loan.loan_balance<0:
            loan.status = "Settled"
            user = User.objects.get(pk=loan.user.id)
            user.loan_limit = user.loan_limit * 1.2
            user.save()
        elif loan.loan_balance>0:
            loan.loan_balance = loan.loan_balance - settlement.amount
        loan.save()

    elif settlement.status == "Pending" or settlement.status == "Failed":
        loan = Loan.objects.get(pk=settlement.loan.id)
        if loan.loan_balance == 0 or loan.loan_balance<0:
            loan.status = "Settled"
        loan.save()

def send_message(to,message):
    username = "onionapp"
    apikey   = "5c8ce53d0963fda2013f418ede4c0cd7d867206c1646f71a51cb647eb0524692"
    gateway = AfricasTalkingGateway(username, apikey)
    try:
        results = gateway.sendMessage(to, message)
    except AfricasTalkingGatewayException:
        print ('Encountered an error while sending')

def monitor_loans():
    today = get_date("%Y-%m-%d",0)
    loans = Loan.objects.all()
    date_format = "%Y-%m-%d"
    for loan in loans:
        if loan.status == "Active":
            due_date = loan.dueDate.strftime('%Y-%m-%d') 
            d1 = datetime.datetime.strptime(today, '%Y-%m-%d')
            d2 = datetime.datetime.strptime(due_date,'%Y-%m-%d')     
            daysDiff = int((d2-d1).days)          

            if  daysDiff < 0: #Loan is Overdue
                daysDiff = daysDiff * -1
                remainder = daysDiff % 30
        
                if remainder == 1: #a day has passed after n months so increment loan
                    #increase loan balance by 20%
                    loan.loan_balance = loan.loan_balance * 1.2
                    loan.save()
                    print('Loan increased because deadline has passed by a month')
                else:
                    print('Severly Late') 
            elif daysDiff <=5 and daysDiff >=1 :
                print ('Deadline Approaching')
                #send reminder

            elif daysDiff == 0:
                print ("D-Day has reached")

        


def get_date(dateFormat="%Y-%m-%d", addDays=0):

    timeNow = datetime.datetime.now()
    if (addDays!=0):
        anotherTime = timeNow + datetime.timedelta(days=addDays)
    else:
        anotherTime = timeNow

    return anotherTime.strftime(dateFormat)

def dummy_task():
    print("Yeey am a dummy task")      








   

  






    



