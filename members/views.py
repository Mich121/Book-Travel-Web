from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import forms
from book.models import Profile
from .forms import ProfilePageForm

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = forms.SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/add_profile.html'
    success_url = reverse_lazy('home')
        
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    form_class = ProfilePageForm
    success_url = reverse_lazy('home')

    def get_object(self):
        user = self.request.user
        return Profile.objects.get(user=user.id)

