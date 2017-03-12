from django.db import models
from django.urls import reverse

class Zvrst(models.Model):
    
    naziv_zvrsti = models.CharField(max_length=200, help_text="Vnos skupine del(Gradbena,Obrtniška,..)")
    splosna_dolocila_zvrsti = models.TextField(max_length=1000,help_text="")
    
    def __str__(self):
                        
        return self.naziv_zvrsti
    def get_absolute_url(self):
        return reverse('zvrst-detail', args=[str(self.id)])   

class Skupina(models.Model):
    
    naziv_skupine = models.CharField(max_length=200, help_text="Vnos skupine del(Zemeljska,Zidarska,..)")
    splosna_dolocila_skupine = models.TextField(max_length=1000,help_text="")
    zvrst = models.ForeignKey('Zvrst', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
                        
        return self.naziv_skupine
    def get_absolute_url(self):
        return reverse('skupina-detail', args=[str(self.id)])   


class VrstaDel(models.Model):
    
    naziv_vrste_del = models.CharField(max_length=200,help_text="Vnos skupine del(Izkopi,Zasipi,..)")
    splosna_dolocila_vrste_del = models.TextField(max_length=1000,help_text="")
    skupina = models.ForeignKey('Skupina', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        
        return self.naziv_vrste_del
        
    def get_absolute_url(self):
        return reverse('vrsta_del-detail', args=[str(self.id)])   

class DelPostavke(models.Model):
 
    kratek_opis_dela_postavke = models.CharField(max_length=100)
    opis_dela_postavke = models.TextField(max_length=1000)
    norma_cas = models.IntegerField(default=0) 
    #postavka = models.ManyToManyField(Postavka)
    splosna_dolocila_dela_postavke = models.TextField(max_length=1000,help_text="")
        

    def __str__(self):
    
        return '%s' % (self.kratek_opis_dela_postavke)

    def get_absolute_url(self):
        
        return reverse('del_postavke-detail', args=[str(self.id)])   


class Postavka(models.Model):
    
    kratek_opis = models.CharField(max_length=100)
    opis_postavke = models.TextField(max_length=1000, help_text="")
    enota_mere = models.CharField(max_length=100)
    norma_cas = models.IntegerField(default=0) 
    vrsta_del = models.ForeignKey('VrstaDel', on_delete=models.SET_NULL, null=True)
    splosna_dolocila_postavke = models.TextField(max_length=1000, help_text="")
    del_postavke = models.ManyToManyField(DelPostavke, help_text="")  
   

    def __str__(self):
    
        return '%s, %s' % (self.kratek_opis, self.opis_postavke)

    def get_absolute_url(self):
        
        return reverse('postavka-detail', args=[str(self.id)])        



