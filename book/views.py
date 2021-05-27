from book.models import Tour
from django.db import models
from django.shortcuts import render
from django.views import generic
from .filters import Filters
# Create your views here.
class Home(generic.ListView):
    model = Tour
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Filters(self.request.GET, queryset=self.get_queryset())
        return context

class CurrentTrip(generic.DetailView):
    model = Tour
    template_name = 'currenttrip.html'

class Book(generic.DetailView):
    model = Tour
    template_name = 'book.html'