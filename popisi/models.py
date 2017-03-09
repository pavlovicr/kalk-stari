from django.db import models
from django.urls import reverse

#Gradbena,obrtniška
class Zvrst(models.Model):
    
    naziv_zvrsti = models.CharField(max_length=200, help_text="Vnos skupine del(Gradbena,Obrtniška,..)")
    splosna_dolocila_zvrsti = models.TextField(max_length=1000,help_text="Enter a brief description of the book")
    
    def __str__(self):
                        
        return self.naziv_zvrsti

#Zemeljska,Zidarska,Betonska
class Skupina(models.Model):
    
    naziv_skupine = models.CharField(max_length=200, help_text="Vnos skupine del(Zemeljska,Zidarska,Betonska,)")
    splosna_dolocila_skupine = models.TextField(max_length=1000,help_text="Enter a brief description of the book")
    zvrst = models.ForeignKey('Zvrst', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
                        
        return self.naziv_skupine


#Izkopi,Zasipi,Odvozi
class VrstaDel(models.Model):
    
    naziv_vrste_del = models.CharField(max_length=200)
    splosna_dolocila_vrste_del = models.TextField(max_length=1000,help_text="Enter a brief description of the book")
    skupina = models.ForeignKey('Skupina', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        
        return self.naziv_vrste_del
    
    
    def get_absolute_url(self):
        
        return reverse('vrsta_del-detajl', args=[str(self.id)])        

class DelPostavke(models.Model):
 
    kratek_opis_dela_postavke = models.CharField(max_length=100)
    opis_dela_postavke = models.TextField(max_length=1000)
    norma_cas = models.IntegerField(default=0) 
    #postavka = models.ManyToManyField(Postavka)
    splosna_dolocila_dela_postavke = models.TextField(max_length=1000,help_text="Enter a brief description of the book")
        

    def __str__(self):
    
        return '%s' % (self.kratek_opis_dela_postavke)



class Postavka(models.Model):
    
    kratek_opis = models.CharField(max_length=100)
    opis_postavke = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    enota_mere = models.CharField(max_length=100)
    norma_cas = models.IntegerField(default=0) 
    vrsta_del = models.ForeignKey('VrstaDel', on_delete=models.SET_NULL, null=True)
    splosna_dolocila_postavke = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    del_postavke = models.ManyToManyField(DelPostavke, help_text="Select a genre for this book")  
   

    def __str__(self):
    
        return '%s, %s' % (self.kratek_opis, self.opis_postavke)

    def get_absolute_url(self):
        
        return reverse('postavka-detail', args=[str(self.id)])        



