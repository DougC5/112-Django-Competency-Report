from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') #tuple

class MovieAdmin(admin.ModelAdmin):
    #exclude = ('price',)
    #fields = ('title', 'price', 'stock')
    list_display = ('title', 'price', 'stock')

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)


