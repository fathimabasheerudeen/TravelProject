

from . models import Place
# Create your views here
from django.http import HttpResponse
from django.shortcuts import render                                              


def demo(request):
     obj=Place.objects.all()
     return render(request,"index.html",{'result':obj})
  #def difference(request):
    # x= int(request.GET['num1'])
    # y= int(request.GET['num2'])
   #  res=x-y
    # return render(request,"result.html",{'result':res})
