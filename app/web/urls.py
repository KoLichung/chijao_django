from django.urls import path
from . import views

urlpatterns = [
    path('privacy_policy_others', views.privacy_policy_others, name='privacy_policy_others'),
]