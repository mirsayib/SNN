from django.contrib import admin

from .models import FriendRequest, FriendList

myModels = [FriendRequest, FriendList]

admin.site.register(myModels)