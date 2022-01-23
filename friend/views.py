from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import FriendList, FriendRequest
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def friends(request):
    return render(request, 'friend/list_friends.html')

@login_required
def send_request(request, pk):
    receiver = User.objects.get(pk=pk)
    sender = request.user

    f = FriendRequest(sender = sender, receiver=receiver)
    FriendRequest.save(f)

    messages.success(request, f'Friend Request Sent to {receiver.username}!')


    return redirect('user_display', pk=receiver.pk)

@login_required
def pending_requests(request):
    return render(request, 'friend/pending_requests.html')

@login_required
def accept_request(request, pk):
    f_request = FriendRequest.objects.get(pk=pk)
    request.user.friendlist.add_friend(f_request.sender)
    f_request.delete()

    messages.success(request, f'Congrats! You are now friends with {f_request.sender}!')


    return redirect('pending-requests')

@login_required
def cancel_request(request, pk):
    receiver = User.objects.get(pk=pk)
    f_request = FriendRequest.objects.get(sender=request.user, receiver=receiver)
    f_request.delete()

    return redirect('user_display', pk=pk)

@login_required
def decline_request(request, pk):
    f_request = FriendRequest.objects.get(pk=pk)
    f_request.delete()

    return redirect('pending-requests')

@login_required
def unfriend(request, pk):
    friend = User.objects.get(pk=pk)
    request.user.friendlist.remove_friend(friend)

    messages.success(request, f'{friend.username} is no longer a friend!')


    return redirect('user_display', pk=friend.pk)



