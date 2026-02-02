from django.shortcuts import render

from django.urls import reverse
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

# Create your views here.
from django.urls import reverse

from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "accounts/profile_detail.html"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ("avatar",)
    template_name = "accounts/profile_form.html"

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.object.pk})

