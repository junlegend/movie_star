import json
from django.http import JsonResponse
from django.views import View
from movies.models import Movie


class Movie(View):
    def get(self, request):
        movies = Movie.objects.all()
        result = []
        for movie in movies:
            result.append(
                {
                    "title": movie.title,
                    "release_date": movie.release_date,
                    "running_time": movie.runnging_time,
                }
            )

        return JsonResponse({"result": result}, status=200)


class Actor(View):
    def get(self, request):
        actors = Actor.objects.all()
        result = []
        for actor in actors:
            result.append(
                {
                    "first_name": actor.first_name,
                    "last_name": actor.last_name,
                    "date_of_birth": actor.date_of_birth,
                }
            )
        return JsonResponse({"result": result}, status=200)
