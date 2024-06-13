from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    print("home")
    context = { 'text' : 'Texto passado por parametro'}
    return render(request,'home.html',context)
