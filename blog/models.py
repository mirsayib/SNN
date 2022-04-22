from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    likes = models.ManyToManyField(User, related_name="blog_likes")
    dislikes = models.ManyToManyField(User, related_name="blog_dislikes")

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:100]
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    def likes_count(self):
        return self.likes.count()
    
    def dislikes_count(self):
        return self.dislikes.count()

class Comment(models.Model):
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    likes = models.ManyToManyField(User, related_name="comment_likes")
    dislikes = models.ManyToManyField(User, related_name="comment_dislikes")


    def __str__(self):
        return f"{self.author}'s comment"
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.post.pk})
    
    def likes_count(self):
        return self.likes.count()
    
    def dislikes_count(self):
        return self.dislikes.count()
    