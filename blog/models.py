from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #Charfield es para definir el numero de caracteres de un texto
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

# Esto va para definir funciones (def)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #str para dato tipo string
    def __str__(self):
        return self.title