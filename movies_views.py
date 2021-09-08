import json
from django.http import JsonResponse
from django.views import View
from movies.models import Movie, Actor


class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        result = []
        for movie in movies:
            starring = []
            actors = Actor.objects.all()
            for actor in actors:
                starring.append({"name": actor.first_name})

            result.append(
                {
                    "1.title": movie.title,
                    "2.release_date": movie.release_date,
                    "3.starring": starring,
                }
            )

        return JsonResponse({"result": result}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(
            title=data["title"],
            release_date=data["release_date"],
            running_time=data["running_time"],
        )

        return JsonResponse({"success": "SUCCESS"}, status=201)


class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        result = []
        for actor in actors:
            movie_starring = []
            movies = Movie.objects.all()
            for movie in movies:
                movie_starring.append({"title": movie.title})
            result.append(
                {
                    "1.first_name": actor.first_name,
                    "2.last_name": actor.last_name,
                    "3.movie_starring": movie_starring,
                }
            )
        return JsonResponse({"result": result}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(
            first_name=data["first_name"],
            last_name=data["last_name"],
            date_of_birth=data["date_of_birth"],
        )

        return JsonResponse({"success": "SUCCESS"}, status=201)
