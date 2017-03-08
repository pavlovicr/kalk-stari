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


def vaja(request):
    a='nasa cetica koraka'       
    return HttpResponse(a)


class PostavkaListView(generic.ListView):
    model = Postavka   

#Poleg osnovnega lista postavka_list dodam še seznam 
    def get_context_data(self, **kwargs):
        
        context = super(PostavkaListView, self).get_context_data(**kwargs)
        context['seznam'] = Postavka.objects.filter(opis_postavke__icontains='izkop')[:1]
        context['vaja1'] = "Vaja 1"
        context['vaja'] = Postavka.objects.filter(opis_postavke__icontains='izkop')[:3]
        context['vaja2'] = "Vaja 2"


        return context
       

class PostavkaFilter(generic.ListView):
    model = Postavka   

    def get_queryset(self):
        return Postavka.objects.filter(opis_postavke__icontains='izkop')[:1]


class P(generic.ListView):
    model = Postavka       
    context_object_name = 'seznam'  
    queryset = Postavka.objects.filter(opis_postavke__icontains='izkop')[:2] 
    template_name = 'popisi/poljubno.html'  

class PostavkaDetailView(generic.DetailView):
    model = Postavka       