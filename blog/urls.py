from django.urls import path, include
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    CommentCreateView,
    PostUpdateView,
    PostDeleteView
)
urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/like/', views.likeView, name='post-like'),
    path('post/<int:pk>/dislike/', views.dislikeView, name='post-dislike'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name="add-comment"),
    path('comment/<int:pk>/edit/', views.editComment, name='edit-comment'),
    path('comment/<int:pk>/delete/', views.deleteComment, name='delete-comment'),
    path('comment/<int:pk>/like/', views.likeViewC, name='comment-like'),
    path('comment/<int:pk>/dislike/', views.dislikeViewC, name='comment-dislike'),
    path('about/', views.about, name="blog-about"),
    path('chat/', include('chat.urls'))
]
