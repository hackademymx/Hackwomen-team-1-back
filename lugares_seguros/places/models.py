from django.db import models

# Create your models here.
class Place (models.Model):
    
    name = models.CharField(max_length =56)
    description = models.CharField (max_length=256)
    address_state =models.CharField(max_length=32)
    address_city =models.CharField(max_length=32)
    address_colonia = models.CharField(max_length=32)
    address_street=models.CharField(max_length=32)
    address_zipcode = models.CharField(max_length=32)

    class Meta:
        db_table = 'places' #este es el nombre de nuestra tabla, es necesario referenciarla para poder verla

        def __str__(self): #definimos la función para retornar el nombre de nuestra tabla, 
            return self.name
        
        #una vez que ya tenemos el modelo en django, hay que definir el serializador. Hay diferentes
        #tipos de serializadores. aquí vamos a trabajar con el serializador basado en modelos
        
        
        
