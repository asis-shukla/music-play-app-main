from django.conf.urls import include
from django.urls.conf import path
from music import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'album', views.AlbumList, basename=None)
router.register(r'songs', views.SongList, basename=None)

urlpatterns = [
    path('', include(router.urls)),
    # path("song/", view=views.SongList.as_view(), name="song"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
