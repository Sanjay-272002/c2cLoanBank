from django.shortcuts import render







def home(request):
    return render(request,'web/home.html')

def profile(request):
    
        return render(request,'web/profile.html')  

def askloan(request):
    return render(request,'web/askloan.html')

def status(request):
    return render(request,'web/status.html')

