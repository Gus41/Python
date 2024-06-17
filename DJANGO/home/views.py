from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from home import data



# Create your views here.

#HOME VIEWS
def home(request):
    context = { 'tittle' : 'Home',
                'posts' : data.posts}
    return render(request,'home.html',context)

def post(request,id):
    context = {'tittle' : "Post"}
    print(id)
    return render(request, 'post.html', context )



