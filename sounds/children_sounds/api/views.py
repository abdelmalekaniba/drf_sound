

from rest_framework.response import Response

from rest_framework.views import APIView
from children_sounds.api.serializers import AlbumSerializer, SoundSerializer
from children_sounds.models import Album, Sound
from rest_framework import status


class AlbumAV(APIView):
   
    def get(self, request):
        platform = Album.objects.all()
        serializer = AlbumSerializer(
            platform, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class SoundAV(APIView):
   

    def get(self, request):
        movies = Sound.objects.all()
        serializer = SoundSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class AlbumDetailAV(APIView):
   

    def get(self, request, pk):
        try:
            movie = Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AlbumSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Album.objects.get(pk=pk)
        serializer = AlbumSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Album.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


