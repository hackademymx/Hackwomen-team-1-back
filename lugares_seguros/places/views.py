from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
<<<<<<< HEAD
from .models import Place
from .serializers import PlaceSerializers
from django.shortcuts import get_object_or_404
=======
from .models import Place 
from.serializers import PlaceSerializers
>>>>>>> 185d4395d98364163e2b7e9e75e963d09e9c30ad

# Create your views here.

class PlaceAPIView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        print(request.data)
        try:
            file = request.data['image']
            request.data['image'] = file
        except KeyError:
            file = None  
        serializer = PlaceSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self,request):
        places = Place.objects.all()
        serializer = PlaceSerializers(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PlaceAPIUpdateDeleteView(APIView):
<<<<<<< HEAD

    def delete(self, request, id):
        place = get_object_or_404(Place, id=id)
        place.delete()
        return Response({'lugar eliminado'}, status=status.HTTP_200_0K)
    
    
=======
>>>>>>> 185d4395d98364163e2b7e9e75e963d09e9c30ad

    def patch(self, request, id):
        place = Place.objects.filter(id=id).first()
        if place is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PlaceSerializers(place, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)