from rest_framework import serializers
from app.models import User,Loan,Settlement,Statement,Activation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","first_name","last_name","national_id","phone_no","email","status","residence","device_id","loan_limit")

class LoanSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Loan
        fields = ("id","user","applicationDate","dueDate","loan_amount","loan_balance","status")

class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = ("id","loan","date","amount","reference","status")

class StatementSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Statement
        fields = ("id","user","details")

class ActivationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Activation
        fields = ("id","user","reference","status")