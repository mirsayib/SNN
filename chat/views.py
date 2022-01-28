from django.shortcuts import render, redirect
from .models import Group, Message
from django.contrib.auth.decorators import login_required

@login_required
def chatroom(request, group_name):
    group = Group.objects.filter(name=group_name).first()
    messages = []

    if(group):
        messages = Message.objects.filter(group=group)
    else:
        group = Group(name = group_name).save()

    return render(request, 'chat/chatroom.html', {'group_name': group_name, 'chats':messages})

@login_required
def chat_home(request):
    if(request.method == 'POST'):
        group_name = request.POST.get("group_name")
        if(group_name):
            group = Group.objects.filter(name=group_name).first()
        else:
            group = Group.objects.filter(name='lobby').first()
        
        
        return redirect(group)
    else:
        group = Group.objects.filter(name='lobby').first()
        messages = []
        if(group):
            messages = Message.objects.filter(group=group)
        else:
            group = Group(name = 'lobby').save()

        return render(request, 'chat/chat_home.html', {'chats': messages})