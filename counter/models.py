from django.db import models
from django.contrib.auth.models import User



class train_tricket(models.Model):

    CHOICES1 = (
        ('Dhaka', 'Dhaka'),
        ('Rajshahi', 'Rajshahi'),
        ('Khulna', 'Khulna'),
        ('Sirajganj', 'Sirajganj'),
        ('Bogura', 'Bogura'),
    )

    CHOICES2 = (
        ('Dhaka', 'Dhaka'),
        ('Rajshahi', 'Rajshahi'),
        ('Khulna', 'Khulna'),
        ('Sirajganj', 'Sirajganj'),
        ('Bogura', 'Bogura'),
    )

    Train_name=models.CharField(max_length=100, blank=False)
    Date=models.DateTimeField(blank=True)
    From= models.CharField(max_length=300, choices = CHOICES1, blank=False)
    To=models.CharField(max_length=300, choices = CHOICES2,blank=False)
    ammound=models.CharField(max_length=100,blank=False)


    def __str__(self):
        return self.Train_name




class user_tricket(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    train_name=models.CharField(blank=False,max_length=200)
    From=models.CharField(blank=False,max_length=200)
    To=models.CharField(blank=False,max_length=200)
    Date=models.CharField(blank=False,max_length=100,null=True)
    time=models.CharField(max_length=100,blank=False)
    adult=models.IntegerField(blank=False)
    child=models.CharField(blank=True,max_length=4, null=True)
    phone=models.CharField(max_length=15,blank=False)
    txid=models.CharField(max_length=100,blank=False)
    

    def __str__(self):
        return self.user.username
    






    
