"""vidly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.models import MovieResource, GenreResource, Order_ItemsResource, OrderResource

movie_resource = MovieResource()
genre_resource = GenreResource()
order_resource = OrderResource()
oi_resource = Order_ItemsResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('api/', include(movie_resource.urls)),
    path('api/', include(genre_resource.urls)),
    path('api/', include(order_resource.urls)),
    path('api/', include(oi_resource.urls)),
]
