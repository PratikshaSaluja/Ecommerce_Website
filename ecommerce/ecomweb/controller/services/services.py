from django.shortcuts import render, redirect
from ecomweb.models import service
def services(request):
    service1 = service.objects.all()
    return render(request, 'services.html' ,  { 'serv100': service1  })