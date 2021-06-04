from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
class TravelAgency(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tour(models.Model):
    FLIGHT_FROM = [
        ('Warszawa', 'Warszawa'),
        ('Katowice', 'Katowice'),
        ('Wrocław', 'Wrocław'),
        ('Gdańsk', 'Gdańsk'),
        ('Kraków', 'Kraków'),
    ]
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    owner = models.ForeignKey(TravelAgency, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    flightfrom = models.CharField(choices=FLIGHT_FROM, max_length=20)
    flightto = models.CharField(max_length=20)
    days = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.title + ' | ' + str(self.owner)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.IntegerField(max_length=12, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    housenumber = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.user)

class Booking(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()

    def __str__(self):
        return self.title + ' | ' + str(self.user)

    @property
    def get_html_title(self):
        return self.title + ' | ' + str(self.user)