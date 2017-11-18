from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User,Loan,Settlement,Statement,Activation


@receiver(post_save, sender=Activation)
def check_activation_status(sender, instance, created, **kwargs):
	activation = instance
	if(activation.status=="Ok"):
		user = User.objects.get(pk=activation.user)
		user.status = "Active"
		user.save()

@receiver(post_save, sender=Settlement)
def check_settlement_status(sender, instance, created, **kwargs):
	settlement = instance
	if(settlement.status=="Ok"):
		loan = Loan.objects.get(pk=settlement.loan)
		loan_balance = loan_balance - settlement.amount
		loan.save()