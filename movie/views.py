import requests
import os

from django.shortcuts import render, get_object_or_404

from .models import Movie
from .serializers import MovieSerializer, MovieEditSerializer

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

API_KEY = os.environ.get('API_KEY')


class MovieListView(generics.ListCreateAPIView):
    """ Class to list movies and create a movie"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveView(generics.RetrieveDestroyAPIView):
    """Class to retrieve and delete a movie"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RankingView(generics.UpdateAPIView):
    """Class to rate a movie

    Args:
        rate (int) : movie taring

    """

    queryset = Movie.objects.all()
    serializer_class = MovieEditSerializer

    def put(self, request, *args, **kwargs):
        rate = request.data.get('rate', 5)

        try:
            rate = int(rate)

        except Exception as e:
            return Response({'error': 'Input valid only with numbers: 0,1,2,3,4,5'}, status=status.HTTP_400_BAD_REQUEST)

        movie_instance = get_object_or_404(Movie, pk=self.kwargs['pk'])
        actual_rate = movie_instance.ranking

        new_ranking = (actual_rate+rate)//2

        serializer = MovieEditSerializer(
            movie_instance,
            data={'ranking': new_ranking}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ApiExternalView(generics.ListAPIView):

    def get(self, request):
        updated_movies = self.call_api_themoviedb()

        if updated_movies:
            for new_movie in updated_movies:
                try:
                    Movie.objects.get(title=new_movie['title'])

                except Exception as e:

                    new_instance = Movie.objects.create(
                        title=new_movie['title'],
                        description=new_movie['description'],
                        image=new_movie['image']
                    )
                    new_instance.save()

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def call_api_themoviedb():
        """
        Method to create movies according to the released in themoviedb

        Return:
            movies_list (list): List of dicts with the new movies
        """

        url = 'https://api.themoviedb.org/3/movie/upcoming?api_key={}&language=en-US&page=1'.format(API_KEY)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            movies_list = []
            for new_movie in data['results']:
                description = new_movie['overview']
                title = new_movie['original_title']
                image = new_movie['poster_path']
                movies_list.append({'description': description, 'title': title, 'image': image})

            return movies_list

