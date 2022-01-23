from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User
from django.utils import timezone

class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="friendlist")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username
    
    def add_friend(self, account):
        """
            Add user in account as a new friend
        """
        if not account in self.friends.all():
            self.friends.add(account)
            account.friendlist.friends.add(self.user)
    
    def remove_friend(self, account):
        """
            remove a friend
        """
        if account in self.friends.all():
            self.friends.remove(account)
            account.friendlist.friends.remove(self.user)
    
    def unfriend(self, removee):
        """
            initiate the action of unfriending removee by remover
        """
        remover_friends_list = self # person terminating the friendship

        #remove removee
        remover_freinds_list.remove_friend(removee)

        # Remove the remover from removee friend list
        friends_list = FriendList.objects.get(user==removee)
        friends_list.remove_friend(self.user)
    
    def is_mutual_friend(self, friend):
        """
            is friend a friend of self.user
        """
        if friend in self.friends.all():
            return True 
        else:
            return False

class FriendRequest(models.Model):
    """
        A friend request has a sender and a reciever
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender") #should be sent instead of sender(related name) #one user can send many requests so we use foreignkey instead of onetoone
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver") #should be recieved instead of receiver(rel name)


    def sender_has_sent_to(self):
        all_sent = self.sender.sender.all()
        users_sent_to = [req.receiver for req in all_sent]

        return users_sent_to
    

    

     


    