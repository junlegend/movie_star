import json
from django.views import View
from django.http  import JsonResponse

from movies.models import Actor, Movie


class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        '''
        results = []
        for actor in actors:
            movie_titles = []
            movies = actor.movies.all()
            for movie in movies:
                movie_titles += [movie.title]
            results += [{
                "first_name"    : actor.first_name,
                "last_name"     : actor.last_name,
                "date_of_birth" : actor.date_of_birth,
                "movie_title"   : movie_titles
            }]
        '''
        results = [
            {
                "first_name"   : actor.first_name,
                "last_name"    : actor.last_name,
                "date_of_birth": actor.date_of_birth,
                "movie_title"  : [movie.title for movie in actor.movies.all()]
            }
        for actor in actors]

        return JsonResponse({'results': results}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        
        Actor.objects.create(
            first_name    = data["first_name"],
            last_name     = data["last_name"],
            date_of_birth = data["date_of_birth"]
        )

        return JsonResponse({"message": "SUCCESS"}, status=201)

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = [
            {
                "title"       : movie.title,
                "release_date": movie.release_date,
                "running_time": movie.running_time,
                "actor_name"  : [actor.first_name for actor in movie.actors.all()]
            }
        for movie in movies]

        return JsonResponse({"results": results}, status=200)

    def post(self, request):
        data = json.loads(request.body)

        Movie.objects.create(
            title        = data["title"],
            release_date = data["release_date"],
            running_time = data["running_time"] 
        )

        return JsonResponse({"message": "SUCCESS"}, status=201)