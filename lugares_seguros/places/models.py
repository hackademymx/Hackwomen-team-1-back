from django.db import models

def upload_load(instance,filename):
    return f'photos_places/{instance.name}/{filename}' #esta es la dirección donde se van a guardar las imágenes

# Create your models here.
class Place (models.Model):
    
    name = models.CharField(max_length =56)
    description = models.CharField (max_length=256)
    address_state =models.CharField(max_length=32)
    address_city =models.CharField(max_length=32)
    address_colonia = models.CharField(max_length=32)
    address_street=models.CharField(max_length=32)
    address_zipcode = models.CharField(max_length=32)
    image= models.ImageField(upload_to=upload_load, default='default.jpg', null=False) #este es el código para llamar la imagen, default=default.jpg es una imagen de default en caso de no obtener ninguna imagen
    
    class Meta:
        db_table = 'places' #este es el nombre de nuestra tabla, es necesario referenciarla para poder verla

        def __str__(self): #definimos la función para retornar el nombre de nuestra tabla, 
            return self.name
        
        #una vez que ya tenemos el modelo en django, hay que definir el serializador. Hay diferentes
        #tipos de serializadores. aquí vamos a trabajar con el serializador basado en modelos
        
        
        
