from django.shortcuts import render

# Create your views here.
def create(request):
    title = request.GET.get('title')
    genre = request.GET.get('genre')
    director = request.GET.get('director')

    movie = Movie(title=title, genre=genre, director=director)
    
    