from book.models import Profile, Tour, Booking
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .filters import Filters
#
from .forms import BookingForm, AddTravelForm
from datetime import datetime
from datetime import timedelta
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Booking
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #get tours from logged travel agency 
        travelagency = self.kwargs['pk']
        tours_in_travel_agency = Tour.objects.filter(owner=self.kwargs['pk'])
        tours = []
        for tour in tours_in_travel_agency:
            tours.append(tour)
        #get today date
        date = datetime.today()
        calendar = Calendar(date.year, date.month, tours)
        #call the formatmonth method, which returns our calendar as a table
        html_calendar = calendar.formatmonth(withyear=True)
        #own html templates is trusted, about 'html_calendar'
        context['calendar'] = mark_safe(html_calendar)
        return context

class Book(generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'book.html'
    success_url = reverse_lazy('home')

    def get_initial(self, *args, **kwargs):
        initial = {}
        title = Tour.objects.get(id=self.kwargs['pk'])
        initial['title'] = title.title
        return initial

class BookEdit(generic.UpdateView):
    model = Booking
    template_name = 'booking_edit.html'
    form_class = BookingForm
    success_url = reverse_lazy('home')

class YourBooking(generic.ListView):
    model = Booking
    template_name = 'your_booking.html'

    def get_context_data(self, *args, **kwargs):
        context = {}
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        book = Booking.objects.filter(user=page_user.user)
        context["book"] = book
        return context

class BookDelete(generic.DeleteView):
    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('home')

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

class AddTravel(generic.CreateView):
    model = Tour
    form_class = AddTravelForm
    template_name = 'addtravel.html'
    success_url = reverse_lazy('home')