from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Place
from .serializers import PlaceSerializer
from rest_framework.parsers import MultiPartParser, FormParser

   
    

class PlaceAPIDeleteView(APIView):
    
    parser_classes= (MultiPartParser, FormParser)
    
    def patch(self, request, id):
        place = Place.objects.filter(id = id).first()
        if place is None:
            return Response({'error': 'Bad request'}, status = status.HTTP_400_BAD_REQUEST)
        place.delete()
        return Response({'message': 'lugar eliminado correctamente'}, status = status.HTTP_200_OK)