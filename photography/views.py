from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def contacts(request):
    return render(request, 'contacts.html')


def works(request):
    return render(request, 'works.html')


def works_bali(request):
    return render(request, 'works-bali.html')


def works_bhutan(request):
    return render(request, 'works-bhutan.html')


def works_jejuri(request):
    return render(request, 'works-jejuri.html')  


def works_purulia(request):
    return render(request, 'works-purulia.html')


# def works_cover(request):
#     return render(request, 'works-cover.html')


def stories(request):
    return render(request, 'stories.html')        


def stories_konyak(request):
    return render(request, 'stories-konyak.html')


def stories_patachitra(request):
    return render(request, 'stories-patachitra.html')


def gallery(request):
    return render(request, 'gallery.html')    


def gallery_festival(request):
    return render(request, 'gallery-festival.html')


def gallery_mood(request):
    return render(request, 'gallery-mood.html')


def gallery_wall_art(request):
    return render(request, 'gallery-wall_art.html')            