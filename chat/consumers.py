from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from time import sleep
import asyncio, json
from .models import Group, Message
from channels.db import database_sync_to_async

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        """
        This handler is called when client initially opens a connection and is
        about finish the websocket handshake
        """
        print('Websocket Connected...', event)
        print("Channel...", self.channel_name) #get default channel_layer from a project

        #add channel to a new or existing group
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        self.user = self.scope["user"]

        async_to_sync(self.channel_layer.group_add)( 
            self.group_name, self.channel_name
        )
        self.send({
            'type': 'websocket.accept'
        })


    
    def websocket_receive(self, event):
        """
        This handler is called when data is received from Client
        """
        data = json.loads(event['text'])

        group = Group.objects.get(name=self.group_name)

        message = Message(
            content = data['msg'],
            group = group,
            author = self.user,
        ).save()

        async_to_sync(self.channel_layer.group_send)(
            self.group_name, 
            {
            'type': 'chat.message',
            'message': event['text']
            }
        )

    def chat_message(self, event):
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })
        

    
    def websocket_disconnect(self, event):
        """
        This handler is called when  either connection to the client is lost,
        either from client closing the connection, or the server or loss of socket
        """
        print('Websocket Disconnected...', event)

        print("Channel name...", self.channel_name, ' disconnected')
        

        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        """
        This handler is called when client initially opens a connection and is
        about finish the websocket handshake
        """
        print(f'{self.channel_name} connected to the websocket')
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        self.user = self.scope["user"]

        await self.channel_layer.group_add( 
            self.group_name, self.channel_name
        )
        await self.send({
            'type': 'websocket.accept'
        })

     
    async def websocket_receive(self, event):
        """
        This handler is called when data is received from Client
        """
        data = json.loads(event['text'])

        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)

        message = Message(
            content = data['msg'],
            group = group,
            author = self.user

        )

        await database_sync_to_async(message.save)()

        await self.channel_layer.group_send(
            self.group_name, 
            {
            'type': 'chat.message',
            'message': event['text']
            }
        )
    
    async def chat_message(self, event):
        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

        

    async def websocket_disconnect(self, event):
        """
        This handler is called when  either connection to the client is lost,
        either from client closing the connection, or the server or loss of socket
        """
        print("Channel name...", self.channel_name, ' disconnected')
        
        await self.channel_layer.group_discard(
            self.group_name, self.channel_name
        )
        raise StopConsumer()
