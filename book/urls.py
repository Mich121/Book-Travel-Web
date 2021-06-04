from book.forms import BookingForm
from django.urls import path, re_path
from .views import AddTravel, BookEdit, Home, CurrentTrip, CalendarView, Book, BookEdit, BookDelete, YourBooking

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('item/<int:pk>/', CurrentTrip.as_view(), name='item'),
    path('book/<int:pk>/', Book.as_view(), name='book'),
    path('booking_edit/<int:pk>/', BookEdit.as_view(), name='booking_edit'),
    path('delete_booking/<int:pk>/', BookDelete.as_view(), name='booking_delete'),
    path('calendar/<int:pk>/', CalendarView.as_view(), name='calendar'),
    path('your_booking/<int:pk>/', YourBooking.as_view(), name='your_booking'),
    path('add_travel/', AddTravel.as_view(), name='add_travel'),
]