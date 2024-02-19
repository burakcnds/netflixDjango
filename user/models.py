from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length = 11)

    def profil_sayac(self):
        return self.profil_set.all().count()

class Profil(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profil-resim')
    owner = models.ForeignKey(CustomUser, on_delete = models.CASCADE)

    def __str__(self):
        return self.title