from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView, LogoutView


class Login(LoginView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('store:filter ')
        return self.render_to_response(self.get_context_data())

    def get_success_url(self):
        return reverse("store:filter", kwargs={'category': 'All'})


class Logout(LogoutView):
    template_name = 'accounts/logout.html'
