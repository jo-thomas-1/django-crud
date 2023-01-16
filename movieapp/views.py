from django.shortcuts import render
from . models import Movie
from . forms import MovieForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        year = request.POST['year']
        desc = request.POST['desc']

        movie = Movie(name=name, image=image, year=year, desc=desc)
        movie.save()

        messages.info(request, name + " has been added")

        return redirect('/add')

    return render(request, 'add.html')

def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'edit.html', {'form': form, 'movie': movie})

def delete(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')

    return render(request, 'delete.html')