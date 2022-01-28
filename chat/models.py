from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Message(models.Model):
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if(self.name == 'lobby'):
            return reverse('chat-home')
        else:
            return reverse("chatroom", kwargs={"group_name": self.name})
    
    