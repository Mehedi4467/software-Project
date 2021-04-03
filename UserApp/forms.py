from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import UserProfile




class User_reg_form(UserCreationForm):
    email=forms.EmailField(max_length=50)
    


    class Meta:
        model=User
        fields=['username','email','password1','password2']
        


class user_update(UserChangeForm):
    class Meta:
        model=User
        fields=['username','email']




class userProfile_UpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields= ['first_name', 'last_name','adress', 'city', 'mobile', 'Bg']
       
