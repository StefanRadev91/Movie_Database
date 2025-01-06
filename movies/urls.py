from django.urls import path
from .views import MovieList, MovieDetail
from .views import MovieSearch
from .views import MovieFavorite
from .views import MovieCategories, MostLikedMovies, NewestMovies
from .views import register
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserList
from .views import MovieDelete
from .views import UserDelete

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    path('movies/search/', MovieSearch.as_view(), name='movie-search'),
    path('movies/<int:pk>/favorite/', MovieFavorite.as_view(), name='movie-favorite'),
    path('movies/categories/', MovieCategories.as_view(), name='movie-categories'),
    path('movies/most-liked/', MostLikedMovies.as_view(), name='most-liked-movies'),
    path('movies/newest/', NewestMovies.as_view(), name='newest-movies'),
    path('movies/<int:pk>/delete/', MovieDelete.as_view(), name='movie-delete'),
    
    path('auth/register/', register, name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),
    
    path('users/', UserList.as_view(), name='user-list'),
]
