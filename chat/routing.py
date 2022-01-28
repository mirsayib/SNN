from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # conventional to start with ws
    path('ws/sc/<str:group_name>/', consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/<str:group_name>/', consumers.MyAsyncConsumer.as_asgi())
]