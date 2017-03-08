from django.db import models
from django.urls import reverse

#Gradbena,obrtniška
class Zvrst(models.Model):
    
    naziv_zvrsti = models.CharField(max_length=200, help_text="Vnos skupine del(Gradbena,Obrtniška,..)")
    splošna_določila_zvrsti = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    
    def __str__(self):
                        
        return self.naziv_zvrsti

#Zemeljska,Zidarska,Betonska
class Skupina(models.Model):
    
    naziv_skupine = models.CharField(max_length=200, help_text="Vnos skupine del(Zemeljska,Zidarska,Betonska,)")
    splošna_določila_skupine = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    zvrst = models.ForeignKey('Zvrst', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
                        
        return self.naziv_skupine


#Izkopi,Zasipi,Odvozi
class VrstaDel(models.Model):
    
    naziv_vrste_del = models.CharField(max_length=200)
    splošna_določila_vrste_del = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    skupina = models.ForeignKey('Skupina', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        
        return self.naziv_vrste_del
    
    
    def get_absolute_url(self):
        
        return reverse('vrsta_del-detajl', args=[str(self.id)])        

class DelPostavke(models.Model):
 
    kratek_opis_dela_postavke = models.CharField(max_length=100)
    opis_dela_postavke = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    norma_cas = models.IntegerField(default=0) 
    #postavkae = models.ManyToManyField(Postavka, help_text="Select a genre for this book")
    splošna_določila_dela_postavke = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
        
    

    def __str__(self):
    
        return '%s' % (self.kratek_opis_dela_postavke)



#Izkop jarkov
class Postavka(models.Model):
    
    kratek_opis = models.CharField(max_length=100)
    opis_postavke = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    enota_mere = models.CharField(max_length=100)
    norma_cas = models.IntegerField(default=0) 
    vrsta_del = models.ForeignKey('VrstaDel', on_delete=models.SET_NULL, null=True)
    splošna_določila_postavke = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    del_postavke = models.ManyToManyField(DelPostavke, help_text="Select a genre for this book")  
   

    def __str__(self):
    
        return '%s, %s' % (self.kratek_opis, self.opis_postavke)

    def get_absolute_url(self):
        
        return reverse('postavka-podrobnosti', args=[str(self.id)])        


class DelDrugace(models.Model):
 
    kratek_opis_dela_postavke = models.CharField(max_length=100)
    opis_dela_postavke = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    norma_cas = models.IntegerField(default=0) 
    postavka = models.ManyToManyField(Postavka)
    splošna_določila_dela_postavke = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
        
    

    def __str__(self):
    
        return '%s' % (self.kratek_opis_dela_postavke)

