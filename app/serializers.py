from rest_framework import serializers
from app.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","first_name","last_name","national_id","phone_no","email","status","residence","device_id","loan_limit")