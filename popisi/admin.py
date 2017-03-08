from django.contrib import admin

from .models import Zvrst,Skupina,VrstaDel,Postavka,DelPostavke,DelDrugace


admin.site.register(Zvrst)
admin.site.register(Skupina)
admin.site.register(VrstaDel)
admin.site.register(Postavka)
admin.site.register(DelPostavke)
admin.site.register(DelDrugace)