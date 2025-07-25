from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from movies.models import Movies

from django.db.models import Q
from operator import attrgetter
from Recommender.views import recommend_user_based_result


def homePageView(request):
    movies = Movies.objects.all()
    user_based_recommendation_list = recommend_user_based_result(request)
    context = {
        'movies': movies[:5],
        'user_based_recommendation_list': user_based_recommendation_list
    }
    return render(request, 'organisation/index.html', context)


def about(request):
    return render(request, 'organisation/aboutus.html', {'title': 'About'})

def aboutus(request):
    return render(request, 'organisation/aboutus.html', {'title': 'AboutUs'})

def contact(request):
    return render(request, 'organisation/contact.html', {'title': 'Contact'})

def index(request):
    return render(request, 'organisation/index.html', {'title': 'Home'})


def movDetail(request):
    return render(request, 'organisation/movieDetail.html', {'title': 'MovieDetail'})

def movGenre(request):
    return render(request, 'organisation/moviesGenre.html', {'title': 'Genre'})

def personDetail(request):
    return render(request, 'organisation/personDetail.html', {'title': 'personDetail'})

def search2(request):
    return render(request, 'organisation/search2.html', {'title': 'search2'})

def SeasonEpisode(request):
    return render(request, 'organisation/SeasonEpisode.html', {'title': 'SeasonEpisode'})

def tvShows(request):
    return render(request, 'organisation/tvShows.html', {'title': 'tvShows'})

def TvShowsDetails(request):
    return render(request, 'organisation/TvShowsDetails.html', {'title': 'TvShowsDetails'})



def search(request):
    context = {}

    query = ""
    if request.GET:
        query = request.GET['search']
        context['query'] = str(query)

        results = sorted(search_bar(query), key=attrgetter('movie_id'), reverse=False)
        context['results'] = results
    return render(request, 'organisation/srch.html', context)


def search_bar(query=None):
    querySet = []
    queries = query.split(" ")
    for q in queries:
        movies = Movies.objects.filter(
            Q(movie_title__icontains=q)
        ).distinct()

        for movie in movies:
            querySet.append(movie)
    return list(set(querySet))
