from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Admin options for booking model """
    fields = ('date', 'time', 'guests', 'table_number',
              'customer', 'name', 'email',
              'special_request', 'location', 'updated')
    list_display = ('name', 'email', 'location', 'date', 'time', 'guests')
    readonly_fields = ('date', 'time', 'guests', 'table_number')
    search_fields = ['name']
    list_filter = ('date', 'guests', 'updated')
    ordering = ('-date', '-time')
    # Allows admin to delete bookings
    actions = ['delete_selected']
