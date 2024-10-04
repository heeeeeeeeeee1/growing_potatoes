from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.

def index(request):
    # 전체 영화 데이터 조회
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES) ## 여기 놓쳤음 기억하기
        if form.is_valid(): # 이게 맞나 -- 틀렸음 기억하기
            form.save() # 유효성 검사에 성공하면 저장하기 -- 틀렸음 기억하기
            return redirect('movies:index') ## 경로 디테일 만들면 수정해주기
         
    else:
        form = MovieForm() # 이게 맞나 -- 틀렸음 기억하기
    context = {
        'form':form,
    }

    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie':movie,
        'form':form,
    }
    return render(request, 'movies/update.html', context)