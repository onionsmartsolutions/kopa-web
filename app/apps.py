from django.apps import AppConfig
from app.signals import check_activation_status, check_settlement_status

class AppConfig(AppConfig):
    name = 'app' 

    def ready(self):
    	post_save.connect(check_activation_status, sender=Activation)
    	post_save.connect(check_settlement_status, sender=Settlement)  