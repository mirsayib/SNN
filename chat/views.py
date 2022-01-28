from django.shortcuts import render
from .models import Group, Message

def chatroom(request, group_name):
    group = Group.objects.filter(name=group_name).first()
    messages = []

    if(group):
        messages = Message.objects.filter(group=group)
    else:
        group = Group(name = group_name).save()

    return render(request, 'chat/chatroom.html', {'group_name': group_name, 'chats':messages}) 