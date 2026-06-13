from django.db import IntegrityError
from django.shortcuts import render , redirect , get_object_or_404
from .models import Movies , Theator , Seat , Booking
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here

def movie_list(request):
    movies = Movies.objects.all()
    
    genre = request.GET.get('genre')
    language = request.GET.get('language')
    
    if genre:
        movies = movies.filter(genre__in=genre)
    
    if language:
        movies = movies.filter(language__in=language)
        
    sort_by = request.GET.get('sort_by')
    
    if sort_by == 'rating':
        movies = movies.order_by('-rating')
    elif sort_by == 'name' :
        movies = movies.order_by('name')
    
    genre_count = movies.values('genre').annotate(total=Count('id')).order_by('genre')
    
    paginator = Paginator(movies , 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj' : page_obj ,
        'genre_count' : genre_count
    }

    return render(request , 'movies/movie_list.html' , context)

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

