from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    print("about")
    return HttpResponse("about View")

