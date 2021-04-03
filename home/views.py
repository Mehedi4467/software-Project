from django.shortcuts import render
from UserApp.models import UserProfile

def index(request):
    indexdata=UserProfile.objects.all()
    context={
        'keydata': indexdata
    }
    return render(request, 'index.html',context)
