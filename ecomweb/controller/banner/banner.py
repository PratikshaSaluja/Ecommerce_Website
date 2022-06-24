from django.shortcuts import render, redirect
from ecomweb.structures.banner import *
def banner(request):
    try:
        banner = banner.objects.values('image')
        return render(request, 'description.html',{'banner' : banner})
    except Exception as E:
        print(E)
        return render(request, 'description.html',{'banner' : banner})
        