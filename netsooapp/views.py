from django.shortcuts import render, redirect


def signup(request): 
    return render(request, 'netsooapp/pages/register/signup.html')


def login_view(request):
     return render(request, 'netsooapp/pages/register/login.html')


def forgot(request):
    return render(request, 'netsooapp/pages/register/forgot.html')

def home(request):
    return render(request, "netsooapp/pages/home.html")

def userProfile(request):
    return render(request , "netsooapp/pages/profile.html")

def payPlan(request):
    return render(request , "netsooapp/pages/payment-plan.html")

def postPlan(request):
    return render(request , "netsooapp/pages/planing.html")

def socialPost(request):
    return render(request , "netsooapp/pages/post-on-social.html")

def faq(request):
    return render(request , "netsooapp/pages/faq.html")


def contactus(request):
    return render(request , "netsooapp/pages/contact.html")

def medium(request):
    return render(request , "netsooapp/pages/medium.html")

def affilatePlan(request):
    return render(request , "netsooapp/pages/affiliate.html")







