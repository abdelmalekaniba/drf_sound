


from django.urls import path

from children_sounds.api.views import AlbumAV, SoundAV ,AlbumDetailAV


urlpatterns = [
    path('Album/',AlbumAV.as_view(),name='Album_list'),
    path('<int:pk>/',AlbumDetailAV.as_view(),name='Album_Detail'),
    path('Sound/',SoundAV.as_view(),name='Sound_list'),
   # path('<int:pk>',movie_detail,name='movie_detail'),

]
