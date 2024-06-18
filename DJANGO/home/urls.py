
from django.http import HttpResponse
from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [ 
    path('',views.home,name='home'),
    path('<int:post_id>/',views.post, name="post")
]