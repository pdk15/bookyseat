from django.db import models
from django.contrib.auth.models import User 


class Movies(models.Model):
    
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Thriller', 'Thriller'),
    ]

    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Korean', 'Korean'),
    ]

    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    name= models.CharField(max_length=255)
    image= models.ImageField(upload_to="movies/")
    rating = models.DecimalField(max_digits=3,decimal_places=1)
    cast= models.TextField()
    description= models.TextField(blank=True,null=True) # optional
    
    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['genre']),
            models.Index(fields=['language']),
        ]

    def __str__(self):
        return self.name

class Theator(models.Model):
    name = models.CharField(max_length=255)
    movies = models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='theators')
    time= models.DateTimeField()

    def __str__(self):
        return f'{self.name} - {self.movies.name} at {self.time}'

class Seat(models.Model):
    theator = models.ForeignKey(Theator,on_delete=models.CASCADE,related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.seat_number} in {self.theator.name}'

class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    seat=models.OneToOneField(Seat,on_delete=models.CASCADE)
    movies =models.ForeignKey(Movies,on_delete=models.CASCADE)
    theator=models.ForeignKey(Theator,on_delete=models.CASCADE)
    booked_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Booking by {self.user.username} for {self.seat.seat_number} at {self.theator.name}'