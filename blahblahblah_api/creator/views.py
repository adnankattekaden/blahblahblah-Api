from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets,status

# Create your views here.


class TestApiView(viewsets.ViewSet):
    def list(self,request):
        pass

    def create(self,request):
        pass
        
