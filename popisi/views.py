from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Zvrst,Skupina,VrstaDel,Postavka,DelPostavke

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



def index(request):
    zvrst1=list(Zvrst.objects.all())
    zvrst=Zvrst.objects.all()
    skupina=Skupina.objects.all()
    vrstadel=VrstaDel.objects.all()
    postavka=Postavka.objects.all()
    delpostavke=DelPostavke.objects.all()
    return render(
        request,
        'index.html',
        context={'zvrst1':zvrst1,'zvrst':zvrst,'skupina':skupina,'vrstadel':vrstadel,'postavka':postavka,'delpostavke':delpostavke,},
    )
#class PostavkaListView(generic.ListView):
#    model = Postavka   
#    def get_context_data(self, **kwargs):
#        context = super(PostavkaListView, self).get_context_data(**kwargs)
#        context['seznam'] = Postavka.objects.filter(opis_postavke__icontains='izkop')[:1]
#        context['vaja1'] = "Tekst Vaja 1"
#        context['vaja'] = Postavka.objects.filter(opis_postavke__icontains='izkop')[:3]
#        context['vaja2'] = "Tekst Vaja 2"
#        return context
class PostavkaFilter(generic.ListView):
    model = Postavka   
    def get_queryset(self):
        return Postavka.objects.filter(opis_postavke__icontains='izkop')[:1]
class PostavkaDetailView(generic.DetailView):
    model = Postavka       

class DelPostavkeDetailView(generic.DetailView):
    model = DelPostavke       

#class VrstaDelListView(generic.ListView):
#    model = VrstaDel       
class VrstaDelDetailView(generic.DetailView):
    model = VrstaDel           

#class SkupinaListView(generic.ListView):
#    model = Skupina       
class SkupinaDetailView(generic.DetailView):
    model = Skupina           

class ZvrstListView(generic.ListView):
    model = Zvrst
class ZvrstDetailView(generic.DetailView):
    model = Zvrst           




# za form

class SkupinaCreate(CreateView):
    model = Skupina
    fields = '__all__'

    zvrst = Zvrst.objects.get(naziv_zvrsti="GRADBENA DELA")
    initial={'zvrst': zvrst,}

class SkupinaUpdate(UpdateView):
    model = Skupina
    fields = ['naziv_skupine','splosna_dolocila_skupine','zvrst']

class SkupinaDelete(DeleteView):
    model = Skupina
    success_url = reverse_lazy('zvrst')




from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ImeForm
def get_ime(request):
    print(request.method) # GET
    if request.method == 'POST':
        form=ImeForm(request.POST)
        if form.is_valid():
            ime = form.cleaned_data['tvoje_ime']
            print(request.method) # POST
            if ime == "janez":
                return HttpResponseRedirect('/popisi/zvrst/')

            else:
                #form=ImeForm()
                return HttpResponse('zivijo')#render(request,'ime.html',{'form':form})
         
    else:
        form=ImeForm()
        return render(request,'ime.html',{'form':form})


    
from .forms import SkupinaForm
def get_skupina(request):
    
    if request.method == 'POST':
        form=SkupinaForm(request.POST)
        if form.is_valid():
            naziv_skupine = form.cleaned_data['naziv_skupine']
            return HttpResponseRedirect('/popisi/skupina/')
    else:
        form=SkupinaForm()
        return render(request,'skupina.html',{'form':form})





