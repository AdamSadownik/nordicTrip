from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offers/', views.OffersList.as_view(), name='offers'),
    path('islandia/', views.islandia, name='islandia'),
    path('norwegia/', views.norwegia, name='norwegia'),
    path('szwecja/', views.szwecja, name='szwecja'),
    path('dania/', views.dania, name='dania'),
    path('blog/', views.blog, name='blog'),
    path('oferta_specjalna/', views.oferta_specjalna, name='oferta_specjalna'),
    path('last_minute/', views.oferta_specjalna, name='last-minute'),
    path('about_us/', views.onas, name='onas'),
]
