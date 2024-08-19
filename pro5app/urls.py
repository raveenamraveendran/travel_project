from django.urls import path

from pro5app import views

urlpatterns = [

    path('',views.index,name='index')

]