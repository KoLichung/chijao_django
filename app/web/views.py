from django.shortcuts import render

# Create your views here.
def privacy_policy_others(request):
    return render(request,'site/privacy_policy_others.html',)