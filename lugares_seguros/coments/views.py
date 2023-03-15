from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Coment
from .serializers import ComentSerializer


# Create your views here.

#vamos a empezar con el mètodo post, que es lo quepide la HU

class ComentView(APIView):
    
    def post(self, request):
        serializer = ComentSerializer(data= request.data)
        serializer.is_valid (raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    