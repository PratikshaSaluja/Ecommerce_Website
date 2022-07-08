from django.shortcuts import render, redirect
from ecomweb.structures.contact import *
from ecomweb.serializers import contactSerializer
from django.views import View
class contact(View):
    def post(self,request):
        try:
            data=request.POST
            serializer = contactSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return redirect("/contact")
            else:
                return render(request, "contact/contact.html")
        except Exception as E:
            return render(request, "contact/contact.html")
    def get(self,request):
         return render(request, "contact/contact.html")