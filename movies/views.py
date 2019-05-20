from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Movie, Genre


def index (request):
    catalog = Movie.objects.all() # read all the table
    # Movie.objects.filter(release_year = 2004)
    # Movie.objects.get(id=1)
    return render(request, 'views/index.html', {'catalog': catalog, 'title': 'Movie Catalog'})

# movie/detail/1
# find object 1 find that object
def detail(request, movie_id):
    #return HttpResponse("im a detail page: " + str(movie_id))
    try:
        the_movie =  Movie.objects.get(id=movie_id)
        return render(request, 'views/detail.html', {'movie': the_movie})

    except Movie.DoesNotExist:
        raise Http404


def genres (request):

    the_genres = Genre.objects.all()
    return render(request, 'views/genre.html', {'genres': the_genres})


def test (request):
    return HttpResponse('<h1>I Am a Test</h1>')


def contact (request):
    return HttpResponse('<h1>I Am a Contact Page</h1>')


def history (request):
    return render(request, 'views/history.html')


def order (request):
    return render(request, 'views/order.html')