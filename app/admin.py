from django.contrib import admin
from django import forms
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

from .models import Loan,User

class UserAdmin(ImportExportActionModelAdmin):
    list_display = ("first_name","last_name","national_id","phone_no","email","status","residence","loan_limit")
    search_fields = ['first_name','last_name','national_id','phone_no','email','residence']

class CustomModelChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "%s %s" % (obj.first_name, obj.last_name)

class LoanAdminForm(forms.ModelForm):
    user = CustomModelChoiceField(queryset=User.objects.all(),label = 'Applicant Name') 

class LoanAdmin(ImportExportActionModelAdmin):
	list_display = ("get_name","applicationDate","dueDate","loan_amount","loan_balance","status")
	form = LoanAdminForm
	search_fields = ["applicationDate","dueDate","loan_amount","loan_balance","status"]
	def get_name(self, obj):
		return obj.user.first_name +'\t\t'+ obj.user.last_name



admin.site.register(Loan,LoanAdmin)
admin.site.register(User,UserAdmin)
