from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/<int:pk>/', views.post_summary),
    path('posts/', views.post_list),
    path('create/post/', views.post_create),
    path('update/post/', views.post_update),
    path('delete/post/', views.post_delete)

]
