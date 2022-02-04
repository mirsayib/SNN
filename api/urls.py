from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/<int:pk>/', views.post_summary),
    path('posts/', views.post_list),
]
