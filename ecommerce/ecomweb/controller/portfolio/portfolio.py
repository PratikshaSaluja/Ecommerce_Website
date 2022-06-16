from django.shortcuts import render, redirect
from ecomweb.models import detail , service
def portfolio(request , productdetail_id):
    service1 = service.objects.all()
    product = detail.objects.filter(pdetailid = productdetail_id ).values('pdetailid','pimage', 'pcategory', 'pclient' , 'pheading', 'pdescription')
    return render(request, 'portfolio-details.html',{'product1' : product,'serv100': service1})