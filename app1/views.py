from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.

def register(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}
    if request.method=='POST' and request.FILES:
        UFO1=UserForm(request.POST)
        PFO1=ProfileForm(request.POST,request.FILES)
        if UFO1.is_valid() and PFO1.is_valid():
            UFO2=UFO1.save(commit=False)
            UFO2.set_password(UFO1.cleaned_data['password'])
            UFO2.save()
            PFO2=PFO1.save(commit=False)
            PFO2.username=UFO2
            PFO2.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('data is not valid')
    return render(request,'register.html',d)


