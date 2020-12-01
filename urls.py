
from django.urls import path

from covi import views

urlpatterns = [
    path('',views.home,name='home'),
    path('us.html',views.usPage,name=''),
    path('india.html',views.indiaPage,name=''),
    path('singapore.html',views.singaPage,name=''),
    path('brazil.html',views.brazPage,name=''),
]