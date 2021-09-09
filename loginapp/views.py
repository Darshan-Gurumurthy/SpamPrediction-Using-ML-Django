from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.views.decorators.cache import cache_control
User = get_user_model()
from django.contrib import messages

import os
import joblib

model1 = joblib.load(os.path.dirname(__file__) + "\\SPalgo1.pkl")
model2 = joblib.load(os.path.dirname(__file__) + "\\SPalgo2.pkl")


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        authUser = authenticate(
            username=username,
            password = password
            )
        if authUser is not None :
           username = request.user.username
           request.session['authdetails'] = username
           login(request,authUser)
           return render(request,'home.html')
        else:
            messages.error(request,'Invalid Credentials')
        return render(request,'login.html')
    return render(request,'home.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        authUser = authenticate(
            username=username,
            password = password
            )
        if authUser is not None :
           login(request,authUser)
           return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
        return render(request,'login.html')
    return render(request,'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def checkSpam(request):
    if(request.method == "POST"):
            algo = request.POST.get("algo")
            rawData = request.POST.get("rawdata")

            if(algo == "SPalgo-1"):
                return render(request, 'output.html', {"answer" : model1.predict([rawData])[0]})
            elif(algo == "SPalgo-2"):
                return render(request, 'output.html', {"answer" : model2.predict([rawData])[0]})
    else:
        return render(request, 'home.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    u = User()
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')


        createNewUser = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
            password = password,


        )
        createNewUser.save()


        return redirect('/')

    return render(request,'register.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutView(request):
    if(request.session.has_key('authdetails') == True):
        request.session.clear()
        print("-----------------")
        # request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def changePassword(request):
    if request.user.is_authenticated:
        username = request.user.username
        if request.method == 'POST':
            newpassword = request.POST.get('password')
            u = User.objects.get(username=username)
            u.set_password(newpassword)
            u.save()
            messages.success(request,'Password Chnaged Please login with new password')
            return render(request,'login.html')




    return render(request,'chnagepassword.html')

def moreAboutuser(request):
    return render(request,'moreAboutuser.html')
