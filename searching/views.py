from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from users.models import Profile
from django.views import View
from django.views.generic import ListView, DetailView
from searching.filters import AlumniFilterDirectorate, AlumniFilterCollege
class CollegeSearchView(LoginRequiredMixin,ListView):
    model = Profile
    template_name = 'searching/college_searching.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AlumniFilterCollege(self.request.GET, queryset=self.get_queryset())
        return context

class DirectorateSearchView(LoginRequiredMixin,ListView):
    model = Profile
    template_name = 'searching/directorate_searching.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AlumniFilterDirectorate(self.request.GET, queryset=self.get_queryset())
        return context

class UserDetailView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'searching/user_detail.html'