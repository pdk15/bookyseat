from django.contrib import admin
from .models import Movies, Theator, Seat, Booking
# Register your models here.

@admin.register(Movies)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','rating','cast','genre']

@admin.register(Theator)
class TheatorAdmin(admin.ModelAdmin):
    list_display= ['name','movies','time']
    
@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):  
    list_display = ['theator','seat_number','is_booked']   

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user','seat','movies','theator','booked_at']    
    
