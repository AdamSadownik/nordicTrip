from django.shortcuts import render
from django.views.generic import ListView

from home.models import Offer


def index(request):
    return render(request, 'home.html')


class OffersList(ListView):
    model = Offer
    template_name = "offers.html"
