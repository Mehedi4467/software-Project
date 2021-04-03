from django.shortcuts import render,redirect
from UserApp.models import UserProfile
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from UserApp.forms import userProfile_UpdateForm,user_update
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from counter.models import user_tricket
@login_required(login_url='/User/login') 
def user_account(request):
    current_user=request.user
    accountData=UserProfile.objects.get(user_id=current_user.id)
    tricketdata=user_tricket.objects.filter(user=request.user)
    context={
        'Ad':accountData,
        'tr':tricketdata
    }

    return render(request,'dashbord.html',context)



@login_required(login_url='/User/login')  # Check login
def userProfile_update(request):
    if request.method == 'POST':
        user_form = user_update(request.POST, instance=request.user)
        profile_form = userProfile_UpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
         
            return redirect('account')
    else:
    
        user_form = user_update(instance=request.user)
       
        profile_form = userProfile_UpdateForm(instance=request.user)
        
        context = {
          
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'profileUpdate.html', context)


@login_required(login_url='/User/log')
def user_password_update(request):
    if request.method == "POST":
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Your Password has been updated!')
            return redirect('account')
        else:
            messages.success(request, 'Please correct the error Below!.')
            return redirect('update_password')

    else:
      form=PasswordChangeForm(request.user) 
      return render(request, 'pass.html',{'form':form})
        



def history(request):

    tricketdata=user_tricket.objects.filter(user=request.user)

    context={
        'train':tricketdata
    }
    return render(request,'train_history.html',context)