from rest_framework import viewsets
from .models import Album, Song
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlbumSerializers, SongSerializers

class AlbumList(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers


class SongList(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializers


#   def get(self, request):
#         songs = Song.objects.all()
#         serializer = SongSerializers(songs, many=True)
#         return Response(serializer.data)
    
#     def post(self):
#         pass  

#     elif request.method == 'POST': # user posting data
#         serializer = CountrySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save() # save to db
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)