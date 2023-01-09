from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'send_mail.html',{'send_mail_to':'Arif'})