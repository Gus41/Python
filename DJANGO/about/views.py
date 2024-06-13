from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    print("about")
    context = { 
        'text' : 'Texto passado por parametro / about',
        'tittle' : 'About'
        }    
    return render(request,'about.html',context)

def more(request):
    print("about/more")
    context = { 
        'text' : 'Texto passado por parametro / about / more',
        'tittle' : 'More'
        }
    return render(request,'more.html',context)