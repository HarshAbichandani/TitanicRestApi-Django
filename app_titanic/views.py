from django.shortcuts import render
from rest_framework import viewsets
from app_titanic.models import Titanic
from app_titanic.serializers import TitanicSerializer
from app_titanic import TiML2
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.
class TitanicViewSet(viewsets.ModelViewSet):
    queryset = Titanic.objects.all().order_by('-id')
    serializer_class = TitanicSerializer
    def create(self,request,*args,**kwargs):
       viewsets.ModelViewSet.create(self,request,*args,**kwargs)
       ob = Titanic.objects.latest('id')
       sur = TiML2.pred(ob)
       return  Response({'status':'Success','Survived': sur,'tmp':args})
