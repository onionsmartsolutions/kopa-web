from django.conf.urls import  include, url
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^loans/$', views.LoanList.as_view()),
    url(r'^loans/(?P<pk>[0-9]+)/$', views.LoanDetail.as_view()),
    url(r'^statements/$', views.StatementList.as_view()),
    url(r'^statements/(?P<pk>[0-9]+)/$', views.StatementDetail.as_view()),
    url(r'^settlements/$', views.SettlementList.as_view()),
    url(r'^settlements/(?P<pk>[0-9]+)/$', views.SettlementDetail.as_view()),
    url(r'^activations/$', views.ActivationList.as_view()),
    url(r'^activations/(?P<pk>[0-9]+)/$', views.ActivationDetail.as_view()),
]