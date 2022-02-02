from django.shortcuts import render, redirect
from .models import Group, Message
from django.contrib.auth.decorators import login_required
from django.contrib import messages as alerts
from .forms import CreateGroupForm


@login_required
def chatroom(request, group_name):
    group = Group.objects.filter(name=group_name).first()
    if(not group):
        alerts.success(request, f'No Group Of Name {group_name} exists')
        return redirect(Group.objects.filter(name='lobby').first())
    else:
        messages = Message.objects.filter(group=group)
        return render(request, 'chat/chatroom.html', {'group_name': group_name, 'chats':messages})

@login_required
def chat_home(request):
    if(request.method == 'POST'):
        group_name = request.POST.get("group_name")
        if(group_name):
            group = Group.objects.filter(name=group_name).first()
            if(not group):
                alerts.success(request, f'No Group Of Name {group_name} exists')
                return redirect('chat-home')
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

@login_required
def create_group(request):
    if(request.method == 'POST'):
        form = CreateGroupForm(request.POST)

        if(form.is_valid()):
            name = request.POST.get("name")
            if(not Group.objects.filter(name=name).first()):
                form.save()
                alerts.success(request, 'Group Created')
                group = Group.objects.filter(name=name).first()
                return redirect(group)
            else:
                alerts.success(request, 'Group Already Exists')
                group = Group.objects.filter(name=name).first()
                return redirect(group)

    else:
        form = CreateGroupForm()
    
    return render(request, 'chat/create_group.html', {'form':form})

@login_required
def dms(request):
    return render('chat/private_chat.html')

    