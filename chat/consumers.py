# chat/consumers.py
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

# database
from channels.db import database_sync_to_async

# models
from .models import ChatModel
from accounts.models import CustomUser

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sender_id = self.scope['user'].id
        self.receiver_id = self.scope["url_route"]["kwargs"]["username"]
        print(f"to jest self.scope: {self.scope}")
        print(f"to jest moje konto:: {self.scope['user'].id}")
        
        if int(self.sender_id) > int(self.receiver_id):
            self.room_name = f'{self.sender_id}-{self.receiver_id}'
        else:
            self.room_name = f'{self.receiver_id}-{self.sender_id}'

        self.room_group_name = f"chat_{self.room_name}"

        # Join room group

        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name, self.channel_name
        # )
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group

        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_group_name, self.channel_name
        # )
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json["message"]
        username = text_data_json['username']
        receiver = text_data_json['receiver']

        # self.send(text_data=json.dumps({"message": message}))

        # Send message to room group
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name, {"type": "chat.message", "message": message}
        # )

        # save messages to database
        group_url = f"chat/{self.room_name}"

        await self.save_message(username, self.room_group_name, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message,
                "username": username
            }
        )

     # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            'username': username
            })) 

    @database_sync_to_async
    def save_message(self, username, thread_name, message):
        chat_obj = ChatModel.objects.create(
            sender=username, message=message, thread_name=thread_name)
        get_user = CustomUser.objects.get(id=self.receiver_id)
