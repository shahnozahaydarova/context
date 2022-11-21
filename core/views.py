from django.shortcuts import render
from .models import *

def func1(request):
    posts = car.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'index1.html',context)

def func2(request):
    post = telephone.objects.all()
    context = {
        'post':post
    }
    return render(request,'index2.html',context)

def func3(request):
    post = flower.objects.all()
    context = {
        'post' : post
    }
    return render(request,'index3.html',context)


def func4(request):
    post = komputer.objects.all()
    context = {
        'post':post
    }
    return render(request,'index4.html',context) 

def func5(request):
    post = TVset.objects.all()
    context = {
        'post':post
    }
    return render(request,'index5.html',context)