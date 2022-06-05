from django.shortcuts import render
from django.views.generic import ListView

from home.models import Offer


def index(request):
    return render(request, 'home.html')

def islandia(request):
    return render(request, 'islandia.html')

def szwecja(request):
    return render(request, 'szwecja.html')

def finlandia(request):
    return render(request, 'finlandia.html')

def norwegia(request):
    return render(request, 'norwegia.html')

def blog(request):
    return render(request, 'blog.html')

def oferta_specjalna(request):
    return render(request, 'oferta_specjalna.html')

def onas(request):
    return render(request, 'onas.html')

class OffersList(ListView):
    model = Offer
    template_name = "offers.html"
