from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length = 100)

    # Modify STR representation of genre objects
    def __str__(self):
        return self.name


class Movie (models.Model):
    title = models.CharField(max_length = 100)
    release_year = models.IntegerField()
    price = models.FloatField()
    stock = models.IntegerField()
    director = models.CharField(max_length = 50)
    # relation between tables
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
       return self.title

class Order (models.Model):
    client_id = models.IntegerField()
    total = models.FloatField()

class Order_Items (models.Model):
    movie_id = models.IntegerField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)




