from django.contrib import admin
from .models import Location, Table


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """ Admin options for location model """

    list_display = ('city', 'country', 'address')
    search_fields = ('city',)
    # Allows admin to delete locations
    actions = ['delete_selected']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """ Admin options for table model """

    list_display = ('id', 'number', 'capacity')
    search_fields = ('number',)
    # Allows admin to delete tables
    actions = ['delete_selected']
