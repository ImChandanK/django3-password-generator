from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html') 

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Uppercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))
    
    length = int(request.GET.get('length'))

    if request.GET.get('Numbers'):
        numlist = [str(x) for x in range(10)]
        characters.extend(numlist)

    if request.GET.get('Specials'):
        spllist = ['!','@','$','%','^','&','*']  
        characters.extend(spllist)    

    thepassword = ''
    x = 0
    while x < length:
        charac = random.choice(characters)
        if charac not in thepassword:
            thepassword += charac
            x += 1
        else:
            continue

    return render(request,'generator/password.html', {'password':thepassword}) 

def aboutus(request):
    return render(request,'generator/aboutus.html')