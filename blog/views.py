from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView
)
from .models import Post, Comment

def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']

@login_required
def likeView(request, pk):
    post = Post.objects.get(pk=pk)
    if(request.user in post.likes.all()):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(Post.objects.get(pk=pk))


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
