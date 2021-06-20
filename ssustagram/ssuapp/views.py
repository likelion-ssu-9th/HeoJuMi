from django.shortcuts import render
from .models import ssuapp
# Create your views here.

def home(request):
    blogs=ssuapp.objects.all()
    return render(request,'base.html',{'blogs':blogs})