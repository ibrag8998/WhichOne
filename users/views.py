from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic

from users import services as s
from users.forms import SignInForm


class SignUpView(s.SignUpViewMixin, generic.View):
    template_name = 'users/signup.html'
    next = reverse_lazy('users:signin')


class SignInView(LoginView):
    template_name = 'users/signin.html'
    authentication_form = SignInForm


class LogOutView(LogoutView):
    next_page = reverse_lazy('users:signin')
