from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'DASHBOARD/main.html')

def admin(request):
    return render(request,'DASHBOARD/admin.html')

def members(request):
    return render(request,'DASHBOARD/members.html')

def archives(request):
    return render(request,'DASHBOARD/archives.html')

def library(request):
    return render(request,'DASHBOARD/library.html')

def content_calender(request):
    return render(request,'DASHBOARD/members.html')

def policy_document(request):
    return render(request,'DASHBOARD/archives.html')


