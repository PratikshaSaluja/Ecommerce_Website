from django.shortcuts import render, redirect
from ecomweb.structures.services import *
def services(request):
    try:
        service1 = service.objects.all()
        return render(request, 'services/services.html' ,  { 'serv100': service1  })
    except Exception as E:
        print(E)
        return render(request, 'services/services.html' ,  { 'serv100': service1  })