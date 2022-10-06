from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def privacy_policy_others(request):
    return render(request,'web/privacy_policy_others.html',)

def index(request):
    return render(request,'web/index.html')

def price(request):
    return render(request,'web/price.html')

def works(request):
    return render(request,'web/works.html')

def contact(request):
    return render(request,'web/contact.html')

def message_sent(request):
    return render(request,'web/message_sent.html')