from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegisterForm

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'users/signup.html'
    success_url = '/'
    success_message = "Your account was created successfully."

    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)
