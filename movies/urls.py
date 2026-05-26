from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list , name = 'movie_list'),
    path('<int:movie_id>/theator/',views.theator_list , name='theator_list'),
    path('theator/<int:theator_id>/seats/book/',views.book_seats, name='book_seats'),
]
