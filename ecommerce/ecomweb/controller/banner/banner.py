from django.shortcuts import render, redirect
from ecomweb.structures.banner import *
def description(request , description_id):
    banner = banner.objects.values('image')
    return render(request, 'description.html',{'desc2' : desc1})