from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('posts/<int:pk>/', views.PostDetail.as_view(),name='post-detail-api'),
    path('posts/', views.PostList.as_view(), name='post-list-api'),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('profiles/', views.ProfileList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail-api'),
    path('users/', views.UserList.as_view(), name='user-list-api'),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
