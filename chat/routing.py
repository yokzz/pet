from django.urls import re_path

from chat import consumers

from chat.routing import websocket_urlpatterns  

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]