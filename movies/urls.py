from django.urls import path
from movies.views import Movie
from movies.views import Movie

urlpatterns = [
    path("", Movie.as_view()),
]
