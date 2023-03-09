#serializers va en plural, ahora vamos a importar el serializador desde rest_framework
from rest_framework import serializers
#ahora debemos importar el modelo que acabamos de crear
from .models import Place
#el punto es para indicarle que de ese directorio vamos a traer nuestra clase creada, que es Place

#ahora vamos a definir el serializador con una clase. las buenas prácticas dicen que debemos agregarle, además del nombre del modelo (Place), la palabra "serializer" para no confundirnos con los nombres al momento de invocar

class PlaceSerializer(serializers.ModelSerializer):
    class Meta: #esta metadata va a contener a cuál modelo es que hace referencia, en qué modelo se va a basar este serializador para trabajar y manipular la información, además, cuáles son los campos que yo quiero que ese serializador tenga
        model = Place
        fields = '__all__' #le indico que trabaje con todos los campos o atributos que definí en el modelo

        #####luego de hacer el primer modelo y serializador, hay que crear las primeras migraciones a la base de datos 
        