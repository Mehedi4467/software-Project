from django.urls import path
from .import views

urlpatterns = [
    path('Register/',views.reg_user, name='reg'),
    path('login/',views.user_login, name='log'),
    path('logout/',views.user_logout, name='logout'),
]
