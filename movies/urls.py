from django.urls import path
from movies.views import MovieView
from movies.views import ActorView

urlpatterns = [
    path("", MovieView.as_view()),
    path("/actors", ActorView.as_view()),
]
