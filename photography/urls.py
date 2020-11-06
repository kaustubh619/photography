from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('services', views.services),
    path('testimonials', views.testimonials),
    path('contacts', views.contacts)
]

