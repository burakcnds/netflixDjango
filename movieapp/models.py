from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 50)
    slug =  AutoSlugField(populate_from='title',unique=True)

    def __str__(self):
        return self.title

    

class Movie(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to= 'movie-resim')
    video = models.FileField(upload_to= 'movie-video')
    description = models.TextField(max_length = 300, blank=True, null=True)
    slug =  AutoSlugField(populate_from='title',unique=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title