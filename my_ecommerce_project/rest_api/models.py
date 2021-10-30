from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length = 200)
    duration = models.FloatField()
    rating = models.FloatField()
    category = models.CharField(max_length = 100, default = 'Action')

    def __str__(self):
        return self.name
