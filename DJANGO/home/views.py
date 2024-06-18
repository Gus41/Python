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

def getPostById(post_id:int):
    for d in data.posts:
        if d['id'] == post_id: 
         return d

def post(request,post_id):
    post = getPostById(post_id)
    context = {'tittle' : "Post", 'posts' : [post]}
    print(post_id)
    print(context)
    return render(request, 'post.html', context )



