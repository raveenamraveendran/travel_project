from django.shortcuts import render
from .models import places
from . models import person
# Create your views here.
def index(request):
    x=places.objects.all()
    y=person.objects.all()
    obj={'result':x,
         'resul':y
         }

    return render(request,'uitgkbjbjbjb.html',{'object':obj})