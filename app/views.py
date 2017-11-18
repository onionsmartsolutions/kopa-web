from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import User,Loan,Statement,Settlement,Activation
from app.serializers import UserSerializer,LoanSerializer,SettlementSerializer,StatementSerializer,ActivationSerializer
from rest_framework import  viewsets,generics


"""
Users API
"""
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


"""
Loans API
"""

class LoanList(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned loans applied by a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Loan.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

"""
Settlement API
"""
class SettlementList(generics.ListCreateAPIView):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer

class SettlementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned loans applied by a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Settlement.objects.all()
        loan = self.request.query_params.get('loan', None)
        if loan is not None:
            queryset = queryset.filter(loan=loan)
        return queryset

class StatementList(generics.ListCreateAPIView):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned loans applied by a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Statement.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset


class StatementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer


class ActivationList(generics.ListCreateAPIView):
    queryset = Activation.objects.all()
    serializer_class = ActivationSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned loans applied by a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Activation.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset


class ActivationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activation.objects.all()
    serializer_class = ActivationSerializer

