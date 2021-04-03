from django.urls import path

from .import views

urlpatterns = [
    path('User_Profile/',views.user_account, name='account'),
    path('User_Profile_Update/',views.userProfile_update, name='update'),
    path('User_Password_Update/',views.user_password_update, name='update_password'),
    path('Tricket_history/',views.history, name='history'),
  
]
