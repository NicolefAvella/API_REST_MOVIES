from django.urls import path, include
from .views import MovieListView, MovieRetrieveView, RankingView, ApiExternalView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie'),
    path('<int:pk>', MovieRetrieveView.as_view(), name='movie_specific'),
    path('ranking/<int:pk>', RankingView.as_view(), name='ranking'),
    path('external_api', ApiExternalView.as_view(), name='external_api'),
]