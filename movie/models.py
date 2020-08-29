from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.URLField(max_length=200)
    ranking = models.IntegerField(
        default=5,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.title

