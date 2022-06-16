from django.shortcuts import render, redirect
from ecomweb.structures.services import *
def services(request):
    service1 = service.objects.all()
    return render(request, 'services.html' ,  { 'serv100': service1  })