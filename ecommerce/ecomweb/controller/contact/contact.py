from django.shortcuts import render, redirect
from ecomweb.structures.contact import *
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['msg']

        Contact = contacts(name=name, email=email, subject=subject, msg=msg)
        Contact.save()
        return redirect("contact/contact")
    else:
        return render(request, "contact/contact.html")