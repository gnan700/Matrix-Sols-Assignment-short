from django.urls import path
from organisation import views

urlpatterns = [
    path('', views.homePageView, name="movien-homepage"),
    path('about/', views.about, name="movien-about"),
    path('aboutus/', views.aboutus, name="movien-aboutus"),
    path('search/', views.search, name="movien-search"),
    path('index/', views.index, name="movien-index"),
    path('movDetail/', views.movDetail, name="movien-movieDetail"),
    path('movGenre/', views.movGenre, name="movien-moviesGenre"),
    path('personDetail/', views.personDetail, name="movien-personDetail"),
    path('search2/', views.search2, name="movien-search2"),
    path('SeasonEpisode/', views.SeasonEpisode, name="movien-SeasonEpisode"),
    path('tvShows/', views.tvShows, name="movien-tvShows"),
    path('TvShowsDetails/', views.TvShowsDetails, name="movien-TvShowsDetails"),
    path('contact/', views.contact,name ="movien-contact")
]
