from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/', views.post_list),
    path('profiles/', views.profile_list),
    path('users/', views.user_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
