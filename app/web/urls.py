from django.urls import path
from . import views

urlpatterns = [
    path('privacy_policy_others', views.privacy_policy_others, name='privacy_policy_others'),
    path('index', views.index, name='index'),
    path('price', views.price, name='price'),
    path('works', views.works, name='works'),
    path('contact', views.contact, name='contact'),
    path('message_sent', views.message_sent, name='message_sent'),

]