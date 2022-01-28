from django.urls import path
from . import views

urlpatterns = [
    path('chat_home/', views.chat_home, name='chat-home'),
    path('<str:group_name>/', views.chatroom, name='chatroom')
]
