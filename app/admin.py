from django.contrib import admin
from django import forms
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

from .models import User,Loan,Settlement,Statement,Activation

class UserAdmin(ImportExportActionModelAdmin):
    list_display = ("first_name","last_name","national_id","phone_no","email","status","residence","loan_limit")
    search_fields = ['first_name','last_name','national_id','phone_no','email','residence']

class UserModelChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "%s %s" % (obj.first_name, obj.last_name)

class LoanModelChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "%s" % (obj.id)

class LoanAdminForm(forms.ModelForm):
    user = UserModelChoiceField(queryset=User.objects.all(),label = 'Applicant Name') 

class LoanAdmin(ImportExportActionModelAdmin):
	list_display = ("get_name","applicationDate","dueDate","loan_amount","loan_balance","status")
	form = LoanAdminForm
	search_fields = ["applicationDate","dueDate","loan_amount","loan_balance","status"]
	def get_name(self, obj):
		return obj.user.first_name +'\t\t'+ obj.user.last_name

class StatementAdminForm(forms.ModelForm):
    user = UserModelChoiceField(queryset=User.objects.all(),label = 'Applicant Name') 

class StatementAdmin(ImportExportActionModelAdmin):
	list_display = ("get_name","details")
	form = StatementAdminForm
	def get_name(self, obj):
		return obj.user.first_name +'\t\t'+ obj.user.last_name

class ActivationAdminForm(forms.ModelForm):
    user = UserModelChoiceField(queryset=User.objects.all(),label = 'Applicant Name') 

class ActivationAdmin(ImportExportActionModelAdmin):
	list_display = ("get_name","reference","status")
	form = ActivationAdminForm
	def get_name(self, obj):
		return obj.user.first_name +'\t\t'+ obj.user.last_name

class SettlementAdminForm(forms.ModelForm):
    Loan = LoanModelChoiceField(queryset=Loan.objects.all(),label = 'Loan Number') 

class SettlementAdmin(ImportExportActionModelAdmin):
	list_display = ("get_loan","date","amount","reference","status")
	form = SettlementAdminForm
	def get_loan(self, obj):
		return obj.loan.id


admin.site.register(Loan,LoanAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Statement,StatementAdmin)
admin.site.register(Activation,ActivationAdmin)
admin.site.register(Settlement,SettlementAdmin)