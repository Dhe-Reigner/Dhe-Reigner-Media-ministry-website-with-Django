from django.shortcuts import render
from .models import PolicyDoc,Video,Poster,Card

# Create your views here.
def main(request):
    return render(request,'DASHBOARD/main.html')

def admin(request):
    return render(request,'DASHBOARD/admin.html')

def members(request):
    return render(request,'DASHBOARD/members.html')

def archives(request):
    video = Video.objects.all()
    post = Poster.objects.all()
    card = Card.objects.all()
    return render(request,'DASHBOARD/archives.html',{
        'video':video,
        'post':post,
        'card':card
    })

def library(request):
    return render(request,'DASHBOARD/library.html')

def content_calender(request):
    return render(request,'DASHBOARD/members.html')

def policy_document(request):
    policyDoc = PolicyDoc.objects.all()
    return render(request,'DASHBOARD/policy_document.html',{
        'policy':policyDoc
    })


