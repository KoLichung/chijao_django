from re import S
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def privacy_policy_others(request):
    return render(request,'web/privacy_policy_others.html',)

def suppervisionbuy_support(request):
    return render(request,'web/suppervisionbuy_support.html',)

def index(request):
    return render(request,'web/index.html')

def price(request):
    return render(request,'web/price.html')

def works(request):
    return render(request,'web/works.html')

def contact(request):
    if request.method == 'POST':
        userName = request.POST.get('customerName')
        email = request.POST.get('customerEmail')
        phone = request.POST.get('customerPhone')
        line = request.POST.get('customerLine')
        subject = request.POST.get('customerSubject')
        message = "name:"+userName + "\n" + "email:"+email + "\n" + "phone:"+phone + "\n" + "line:"+line + "\n" + "subject:"+subject + "\n"
        from mailapp.tasks import send_test_mail
        send_test_mail('網站新案件:'+userName, message)
        return redirect('message_sent')

    return render(request,'web/contact.html')

def message_sent(request):
    return render(request,'web/message_sent.html')