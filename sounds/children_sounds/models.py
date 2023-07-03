from django.db import models

# Create your models here.
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    
    

    def __str__(self):
        return self.name


class Sound(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="album")
    audioname = models.FileField(upload_to ='uploads/')
    sound = models.FileField(upload_to ='sound/')
    image = models.ImageField(upload_to='images/')
    
    
    def __str__(self):
        return self.name