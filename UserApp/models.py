from django.db import models
from django.contrib.auth.models import User




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=False)

    adress = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=200, blank=True)
    mobile=models.CharField(max_length=15, blank=True)

    Bg=models.CharField(max_length=5,blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='user_image/')

    def __str__(self):
        return self.user.username




        


    
