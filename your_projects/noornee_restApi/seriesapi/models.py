from django.db import models

# Create your models here.

class Series(models.Model):
    series_genre = (
            ('Action', 'action'),
            ('Horror', 'horror'),
            ('Comedy', 'comedy'),
            ('Animation', 'animation'),
            ('Adventure', 'adventure')
            )
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50, default='1hr')
    genre = models.CharField(max_length=50, choices=series_genre)
    rating = models.FloatField()
    number_of_episodes = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self)->str:
        return f"{self.title}"
