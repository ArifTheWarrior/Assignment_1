from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'show_logs.html',{'name':'page1'})

def Hthreat(request):
    return render(request,'Hthreat.html')

def Lthreat(request):
    return render(request,'Lthreat.html')