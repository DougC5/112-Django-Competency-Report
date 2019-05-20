from django.db import models
from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from movies.models import Movie, Genre, Order, Order_Items

class MovieResource(ModelResource):
    class Meta:
        resource_name = 'movies'
        queryset = Movie.objects.all()
        #excludes = ['price']
        filtering = {'price': ALL, 'stock': ALL}
        #authentication = BasicAuthentication()

class GenreResource(ModelResource):
    class Meta:
        resource_name = 'genre'
        queryset = Genre.objects.all()
        #excludes = ['price']
        filtering = {'price': ALL, 'stock': ALL}
        #authentication = BasicAuthentication()

class Order_ItemsResource(ModelResource):
    class Meta:
        resource_name = 'orderitems'
        queryset = Order_Items.objects.all()
        #excludes = ['price']
        #filtering = {'price': ALL, 'stock': ALL}
        #authentication = BasicAuthentication()

class OrderResource(ModelResource):
    class Meta:
        resource_name = 'orders'
        queryset = Order.objects.all()
        allowed_methods = ['get', 'post', 'patch', 'delete']
        #excludes = ['price']
        #filtering = {'price': ALL, 'stock': ALL}
        authorization = Authorization()