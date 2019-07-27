from django.contrib import admin
from .models import Post

admin.site.register(Post)

# Register your models here.
# Poner en terminal 'python manage.py runserver' para que se actualice el servidor.