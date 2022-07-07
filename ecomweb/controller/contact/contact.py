from django.shortcuts import render, redirect
from ecomweb.structures.contact import *
from ecomweb.serializers import contactSerializer
def contact(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            msg = request.POST['msg']
            Contact = contacts(name=name, email=email, subject=subject, msg=msg)
            serializer = contactSerializer(Contact)
            data=serializer.data
            print(serializer.data,"_________________________") 
            serializer.is_valid()
            serializer.save(data=data)
            return redirect("/contact")
        else:
            return render(request, "contact/contact.html")
    except Exception as E:
        print(E)
        return render(request, "contact/contact.html")