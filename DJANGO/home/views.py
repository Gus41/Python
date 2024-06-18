from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render
from home import data
from typing import Any


# Create your views here.

#HOME VIEWS
def home(request : HttpRequest):
    context = { 'tittle' : 'Home',
                'posts' : data.posts}
    return render(request,'home.html',context)

def getPostById(post_id:int) -> Any:
    for d in data.posts:
        if d['id'] == post_id: 
         return d

def post(request : HttpRequest,post_id : int):
    post = getPostById(post_id) or None

    if post is None:
       raise Http404("Post não existe")
    

    context = {'tittle' : post['title'], 'posts' : [post]}
    print(post_id)
    print(context)
    return render(request, 'post.html', context )



