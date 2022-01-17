from django.urls import path, include
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    CommentCreateView
)
urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/like', views.likeView, name='post-like'),
    path('post/<int:pk>/dislike', views.dislikeView, name='post-dislike'),
    path('post/<int:pk>/comment', CommentCreateView.as_view(), name="add-comment"),
    path('about/', views.about, name="blog-about"),
]
