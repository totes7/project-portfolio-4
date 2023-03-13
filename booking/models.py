from django.db import models
from django.contrib.auth.models import User
from location.models import Location, Table
from datetime import date


class Booking(models.Model):
    """ Model to place reservation """

    # Choices for the time of booking
    BOOKING_TIME = ((1, "12:00 - 14:00"),
                    (2, "14:00 - 16:00"),
                    (3, "18:00 - 20:00"),
                    (4, "20:00 - 22:00"))

    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='booking_customer')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                 related_name='location_name')
    date = models.DateField(default=date.today)
    time = models.IntegerField(choices=BOOKING_TIME, default=1)
    guests = models.IntegerField(default=1)
    special_request = models.TextField(max_length=200, blank=True)
    table_number = models.ManyToManyField(Table, related_name='booked_table')
    updated = models.BooleanField(default=True)

    class Meta:
        """ Order bookings by date """
        ordering = ['date']

    def __str__(self):
        return f"Booking ID: {self.id}"
