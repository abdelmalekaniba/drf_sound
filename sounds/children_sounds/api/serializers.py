from rest_framework import serializers

from children_sounds.models import Album, Sound





class SoundSerializer(serializers.ModelSerializer):
    

    
    #watchlist= serializers.StringRelatedField(many=True)
    class Meta:
        model = Sound
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
   
    album= SoundSerializer(many=True)
    class Meta:
        model = Album 
        fields = "__all__"
        