<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterUserSerializer

# Create your views here.


class RegisterUserView(APIView):
     
     def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Usuario registrado."}, status=status.HTTP_201_CREATED)


class LoginUserView(APIView):
    
      def post(self, request):
         serializer = LoginUserSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         username = serializer.data["username"]
         password = serializer.data["password"]
         
         user = authenticate(username = username, password = password)

         if username is None:
             return Response({"error":"Credenciales inválidas."}, status=status.HTTP_400_BAD_REQUEST)
         
         data = {
             'id': user.id,
             'username': user.username
         }

         return Response(data, status=status.HTTP_200_OK)
>>>>>>> b90613e8ab3811348bf34a27e57a3f3b724c9d1f
