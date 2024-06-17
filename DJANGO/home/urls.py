
from django.http import HttpResponse
from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [ 
    path('',views.home,name='home'),
    path('post/<int:id>',views.post, name="post")
]