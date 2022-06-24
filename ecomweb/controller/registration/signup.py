from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View


def signup(request):
    try:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Please try with some other Username . This Username is already taken.')
                    return redirect('/signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Please try with some other Email . This Email is already taken.')
                    return redirect('/signup')
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,  email=email, username=username, password=password1)
                    user.save()
                    print("user successfully registered ")
            else:
                    messages.info(request,"Your passwords didn't match . Please fill the same passwords.")
                    return redirect('registration/sign-up')
            return redirect('/login')
        else:
            return render(request, "registration/sign-up.html")
    except Exception as E:
        print(E)
        return render(request, "registration/sign-up.html")