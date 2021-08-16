from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Contact
    
def index(request):
    context = {

    }
    return render(request, 'index.html', context)
    #return HttpResponse('This Home Page')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('This About Page')

def skills(request):
    return render(request, 'skills.html')
    #return HttpResponse('This skills Page')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,
        date= datetime.today())
        contact.save()

    return render(request, 'contact.html') 
    #return HttpResponse('This Contact Page')