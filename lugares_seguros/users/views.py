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