from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Zvrst,Skupina,VrstaDel,Postavka,DelPostavke

def index(request):
    zvrst=Zvrst.objects.all()
    skupina=Skupina.objects.all()
    vrstadel=VrstaDel.objects.all()
    postavka=Postavka.objects.all()
    delpostavke=DelPostavke.objects.all()
    return render(
        request,
        'index.html',
        context={'zvsrst':zvrst,'skupina':skupina,'vrstadel':vrstadel,'postavka':postavka,'delpostavke':delpostavke,},
    )
class PostavkaListView(generic.ListView):
    model = Postavka   
#poleg osnovnega dodamo še seznam in vaja1 , vaja in vaja2 
    def get_context_data(self, **kwargs):
        context = super(PostavkaListView, self).get_context_data(**kwargs)
        context['seznam'] = Postavka.objects.filter(opis_postavke__icontains='izkop')[:1]
        context['vaja1'] = "Tekst Vaja 1"
        context['vaja'] = Postavka.objects.filter(opis_postavke__icontains='izkop')[:3]
        context['vaja2'] = "Tekst Vaja 2"
        return context
class PostavkaFilter(generic.ListView):
    model = Postavka   
    def get_queryset(self):
        return Postavka.objects.filter(opis_postavke__icontains='izkop')[:1]
class PostavkaDetailView(generic.DetailView):
    model = Postavka       

class VrstaDelListView(generic.ListView):
    model = VrstaDel       
class VrstaDelDetailView(generic.DetailView):
    model = VrstaDel           

class SkupinaListView(generic.ListView):
    model = Skupina       
class SkupinaDetailView(generic.DetailView):
    model = Skupina           

class ZvrstListView(generic.ListView):
    model = Zvrst
class ZvrstDetailView(generic.DetailView):
    model = Zvrst           