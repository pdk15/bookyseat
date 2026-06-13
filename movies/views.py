from django.db import IntegrityError
from django.shortcuts import render , redirect , get_object_or_404
from .models import Movies , Theator , Seat , Booking
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here

from django.core.paginator import Paginator
from django.db.models import Count

def movie_list(request):

    movies = Movies.objects.all()

    selected_genres = request.GET.getlist('genre')
    selected_languages = request.GET.getlist('language')

    if selected_genres:
        movies = movies.filter(genre__in=selected_genres)

    if selected_languages:
        movies = movies.filter(language__in=selected_languages)

    sort = request.GET.get('sort')

    if sort:
        movies = movies.order_by(sort)

    genres = (
        Movies.objects.values('genre')
        .annotate(total=Count('id'))
        .order_by('genre')
    )

    languages = (
        Movies.objects.values('language')
        .annotate(total=Count('id'))
        .order_by('language')
    )

    paginator = Paginator(movies, 6)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'page_obj': page_obj,
        'genres': genres,
        'languages': languages,
        'selected_genres': selected_genres,
        'selected_languages': selected_languages,
    }

    return render(request, 'movies/movie_list.html', context)
def theator_list(request , movie_id):
    movie = get_object_or_404(Movies , id=movie_id)
    theators = Theator.objects.filter(movies=movie)
    return render(request , 'movies/theator_list.html',{'movie':movie , 'theators':theators})

@login_required(login_url='movies/login')
def book_seats(request , theator_id):
    theator = get_object_or_404(Theator , id = theator_id)
    seats = Seat.objects.filter(theator=theator)
    if request.method == 'POST':
        selected_seats = request.POST.getlist('seats')
        error_seats = []
        if not selected_seats :
            error_message = "Please select at least one seat to book."
            return render(request , 'movies/book_seats.html',{'theator':theator , 'seats':seats , 'error_message':error_message})   
        for seat_id in selected_seats:
            seat = get_object_or_404(Seat , id=seat_id)
            if seat.is_booked :
                error_seats.append(seat.seat_number)
                continue
            try:
                Booking.objects.create(
                    user = request.user,
                    seat = seat ,
                    movies = theator.movies ,
                    theator = theator
                )
                seat.is_booked = True
                seat.save()
            except IntegrityError :
                error_seats.append(seat.seat_number)
        if error_seats :
            error_message = f"The following seats are already booked: {', '.join(error_seats)}"
            return render(request , 'movies/book_seats.html',{'theator':theator , 'seats':seats , 'error_message':error_message})   
        return redirect('profile')  
    return render(request , 'movies/book_seats.html',{'theator':theator , 'seats':seats})

