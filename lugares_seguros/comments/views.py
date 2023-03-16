from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from.serializers import CommentSerializers

# Create your views here.


class CommentView(APIView):
     def post(self, request):
        serializer = CommentSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommentAPIUpdateView(APIView):

   def patch(self, request, id):
      comment = Comment.objects.filter(id=id).first
      if not comment:
         return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
      serializer = CommentSerializers(comment, data=request.data, partial=True)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)