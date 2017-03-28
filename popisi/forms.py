from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
class ImeForm(forms.Form):
    tvoje_ime = forms.CharField(label='vaše uporabniško ime', max_length=10)
    geslo = forms.CharField(label='geslo', max_length=10)


# v python manage.py shell sem prišel na tak način
# from django import forms 
# from popisi.forms import ImeForm


from popisi.models import Skupina
from django.forms import ModelForm

class SkupinaForm(ModelForm):
    class Meta:
        model = Skupina
        fields = ['naziv_skupine', 'splosna_dolocila_skupine', 'zvrst']
       