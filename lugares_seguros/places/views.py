from django.shortcuts import render

# Create your views here.
<<<<<<< Updated upstream
=======
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Place
from .serializers import PlaceSerializer
from rest_framework.parsers import MultiPartParser, FormParser

places = Place.objects.all()
    serializer = PlaceSerializer(places,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    

class PlaceAPIDeleteView(APIView):
    
    parser_classes= (MultiPartParser, FormParser)
    
    def patch(self, request, id):
        place = Place.objects.filter(id = id).first()
        if place is None:
            return Response({'error': 'Bad request'}, status = status.HTTP_400_BAD_REQUEST)
        place.delete()
        return Response({'message': 'lugar eliminado correctamente'}, status = status.HTTP_200_OK)
>>>>>>> Stashed changes
