from django.db import models

class Sala(models.Model):   
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    qtd_computadores = models.IntegerField()
   
    def __str__(self):        
        return '{0}'.format(self.name)
