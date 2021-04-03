from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages
from .forms import User_reg_form

def reg_user(request):
    form = User_reg_form(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_raw)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.save()
            return redirect('home')
        else:
             messages.warning(request, "Password And re Password does not mach")
    context={
        'form':form
    }
    return render(request,'reg.html',context)



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "User Name or Passwod Incarret")

    return render(request,'log.html')





def user_logout(request):
    logout(request)
    return redirect('home')


