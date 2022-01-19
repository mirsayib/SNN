from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment
from .forms import CommentUpdateForm

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
        if(request.user in post.dislikes.all()):
            post.dislikes.remove(request.user)

    return redirect(Post.objects.get(pk=pk))

@login_required
def dislikeView(request, pk):
    post = Post.objects.get(pk=pk)
    if(request.user in post.dislikes.all()):
        post.dislikes.remove(request.user)
    else:
        if(request.user in post.likes.all()):
            post.likes.remove(request.user)
        post.dislikes.add(request.user)
    return redirect(Post.objects.get(pk=pk))

@login_required
def likeViewC(request, pk):
    comment = Comment.objects.get(pk=pk)
    if(request.user in comment.likes.all()):
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
        if(request.user in comment.dislikes.all()):
            comment.dislikes.remove(request.user)

    return redirect(comment.post)

@login_required
def dislikeViewC(request, pk):
    comment = Comment.objects.get(pk=pk)
    if(request.user in comment.dislikes.all()):
        comment.dislikes.remove(request.user)
    else:
        comment.dislikes.add(request.user)
        if(request.user in comment.likes.all()):
            comment.likes.remove(request.user)

    return redirect(comment.post)



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

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True 
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True 
        else:
            return False

@login_required
def deleteComment(request, pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if(request.user == comment.author):
        comment.delete()
        return redirect(post)
    else:
        return HttpResponse("<h1>You Can't Delete Someone Else's Comment</h1>")


@login_required
def editComment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if(request.user == comment.author):
        if(request.method == 'POST'):
            form = CommentUpdateForm(request.POST, instance=comment)
            if(form.is_valid()):
                form.save()
                messages.success(request, 'Comment Updated Successfully')

                return redirect(comment.post)
        else:
            form = CommentUpdateForm(instance=comment)
        
        context = {
            'form': form
        }

        return render(request, 'blog/edit_comment.html', context)
    else:
        return HttpResponse("<h1>You Can't Edit Someone Else's Comment</h1>")






def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
