from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from home import data



# Create your views here.
def home(request):
    print("home")
    context = { 'tittle' : 'Home',
                'posts' : data.posts}
    return render(request,'home.html',context)
