from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserSignUpForm
from django.urls import reverse_lazy

class UserCreationView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'