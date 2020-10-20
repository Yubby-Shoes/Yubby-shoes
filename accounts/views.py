from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class Login(LoginView):
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    template_name = 'accounts/logout.html'
