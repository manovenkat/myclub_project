from django.contrib import admin

# Register your models here.

from events.models import Venue, Event, MyClubUser

# admin.site.register(Venue)
# admin.site.register(Event)
admin.site.register(MyClubUser)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # fields = (('name','venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)

    fieldsets = (
        ('Required Information', {
            'description': "These fields are required for each event.",
            'fields': (('name', 'venue'), 'event_date')
        }),
        ('Optional Information', {
            'classes':('collapse',),
            'fields': ('description', 'manager')
        })
    )