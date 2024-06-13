from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def about(request):
    print("about")
    return render(request,'about.html')

def more(request):
    print("about/more")
    return render(request,'more.html')