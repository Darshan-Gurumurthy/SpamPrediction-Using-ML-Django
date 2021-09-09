from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='homePage'),
    path('login/',loginView,name='loginPage'),
    path('register/',register,name='registerPage'),
    path('logout/',logoutView,name='logoutPage'),
    path('check',checkSpam,name='checkSpam'),
    path('changePassword/',changePassword,name='changePasswordPage'),
    path('moreAboutuser/',moreAboutuser,name='moreAboutuserPage')
]
