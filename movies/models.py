from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='movie_covers/', null=True, blank=True)
    favorite = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

