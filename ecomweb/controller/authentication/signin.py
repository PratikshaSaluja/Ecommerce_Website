from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View

def login(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
                request.session['user_id'] = user.id
                request.session['username'] = username
                return redirect('/')
            else:
                messages.info(request,'Invalid Credentials . Please fill the correct username and password.')
                return redirect('login')
        else:
            return render(request, 'login/signin.html')
    except Exception as E:
        print(E)
        return render(request, 'login/signin.html')
@login_required(login_url='/login')
def logout(request):
    try:
        auth.logout(request)
        return redirect('/')
    except Exception as E:
        print(E)
        return redirect('/')