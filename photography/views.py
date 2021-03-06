from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def send_message(request):
    if request.POST.get('email'):
        mail_subject = "Sudip Saha Photography"
        message = "Name - " + str(request.POST.get('name')) + ", Phone - " + str(request.POST.get('phone')) + ", Email - " + str(request.POST.get('email')) + ", \nMessage - " + str(request.POST.get('message'))
        to_email = "sudip07saha@gmail.com"
        to_list = [to_email]
        from_email = settings.EMAIL_HOST_USER
        send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
    return HttpResponse("Message Send Successfully!")


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


def picture_perfect_india(request):
    return render(request, 'picture-perfect-india.html')


def picture_perfect_india_jejuri(request):
    return render(request, 'picture-perfect-india-jejuri.html')  


def picture_perfect_india_purulia(request):
    return render(request, 'picture-perfect-india-purulia.html')    