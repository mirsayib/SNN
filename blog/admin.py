from django.contrib import admin
from .models import Post, Comment

# Register your models here.
myModels = [Post, Comment]
admin.site.register(myModels)


