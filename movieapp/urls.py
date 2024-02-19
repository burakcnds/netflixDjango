from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('movie/<int:id>/',movie,name='movie'),
    path('movie-detial/<str:d_slug>/',movie_detial,name='movie-detial'),
    path('search/',search,name='search')
]