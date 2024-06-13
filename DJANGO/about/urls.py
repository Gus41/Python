
from django.http import HttpResponse
from . import views
from django.urls import path

urlpatterns = [ 
    path('',views.about),
    path('more/',views.more)
]