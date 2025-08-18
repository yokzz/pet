import json

from django.contrib.auth.models import User

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import ChatRoom, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        room_name = self.scope["url_route"]["kwargs"]["room_name"]
        user = self.scope["user"]
        
        if not user.is_authenticated:
            return
        
        room = await database_sync_to_async(ChatRoom.objects.get)(name=room_name)
        
        db_user = await database_sync_to_async(User.objects.get)(id=user.id)
        
        msg = await database_sync_to_async(Message.objects.create)(
            room=room,
            user=db_user,
            content=message,
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat.message",
                "message": message,
                "user_id": db_user.id,
                "username":
                    db_user.username,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "user_id": event["user_id"],
            "username": event["username"],
        }))