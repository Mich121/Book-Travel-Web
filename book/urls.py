from django.urls import path
from .views import Home, CurrentTrip, Book

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('item/<int:pk>/', CurrentTrip.as_view(), name='item'),
    path('book/<int:pk>/', Book.as_view(), name='book'),
]