
from django.http import HttpResponse
from . import views
from django.urls import path

app_name = 'about'
urlpatterns = [ 
    path('',views.about,name='about'),
    path('more/',views.more,name='more')
]