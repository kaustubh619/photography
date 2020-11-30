from django.urls import path
from . import views

urlpatterns = [
    path('send-message', views.send_message),
    path('', views.index),
    path('about', views.about),
    # path('services', views.services),
    # path('testimonials', views.testimonials),
    path('contacts', views.contacts),
    path('works', views.works),
    path('works-bali', views.works_bali),
    path('works-bhutan', views.works_bhutan),
    path('works-jejuri', views.works_jejuri),
    path('works-purulia', views.works_purulia),
    # path('works-cover', views.works_cover),
    path('stories', views.stories),
    path('stories-konyak', views.stories_konyak),
    path('stories-patachitra', views.stories_patachitra),
    path('gallery', views.gallery),
    path('gallery-festival', views.gallery_festival),
    path('gallery-mood', views.gallery_mood),
    path('gallery-wall_art', views.gallery_wall_art)
]

