from django.shortcuts import render,redirect
from .models import*
from user.models import Profil
from django.db.models import Q

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('profil')

    return render(request,'index.html')

def movie(request,id):
    profil = Profil.objects.get(id = id)
    profiller = request.user.profil_set.all()
    print(profil)
    # tüm filmler
    filmler = Movie.objects.all()
    # kategoriye göre
    kategori = Category.objects.get(title = 'Komedi')
    komedi_film =Movie.objects.filter(category = kategori)
    context = {
        'filmler':filmler,
        'komedi_film':komedi_film,
        'profil':profil,
        'profiller':profiller,
        'id':id
    }
    return render(request,'movie.html',context)

def movie_detial(request,d_slug):
    film = Movie.objects.get(slug = d_slug)
    # profil = Profil.objects.get(id = id)
    # profiller = request.user.profil_set.all()
    print(film)
    context = {
        
        'film':film,
        # 'profil':profil,
        # 'profiller':profiller,
        
    }
    return render(request,'moviedetial.html',context)


def search(request):
    if 'search' in request.GET and request.GET.get('search'):
        q = request.GET.get('search')
        filmler = Movie.objects.filter(
            Q(title__icontains = q) |
            Q(description__icontains = q)
            )
        print(filmler)

    else:
        q = request.GET.get('search')

    context = {
        'filmler':filmler,
        'q':q
    }
    return render(request,'search.html',context)