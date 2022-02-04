from django.urls import path, include
from . import views

urlpatterns = [
    path('post/info/<int:pk>/', views.post_summary),
    path('post/list/', views.post_list),
]
