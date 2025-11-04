from django.db import models

# Create your models here.
class PolicyDoc(models.Model):
    title = models.CharField(max_length=50,blank=True)
    images = models.ImageField(upload_to='images',default=True)
    documents = models.FileField(upload_to='documents',default=True)


    def __str__(self):
        return self.title
    

class Video(models.Model):
    original_video = models.AutoField
    shorts = models.AutoField


    def __str__(self):
        return self.original_video
    
class Poster(models.Model):
    poster = models.ImageField(upload_to='posters')

    def __str__(self):
        return self.poster
    

class Card(models.Model):
    card = models.ImageField(upload_to='cards')

    def __str__(self):
        return self.card
    