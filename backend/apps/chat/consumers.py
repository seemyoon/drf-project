# view for connecting sockets
from channels.db import database_sync_to_async
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer


class ChatConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        self.room_name = None  # None for default
        self.user_name = None

    async def connect(self):
        # self has scope as well
        if not self.scope['user']:
            return await self.close()  # perhaps SocketToken was expired and now we have no user

        # return await super().connect() # it calls 'accept', which accepts connection
        await self.accept() # we connected
        # return print(self.scope)
        # {'type': 'websocket', 'path': '/api/chat/asd/', 'raw_path': b'/api/chat/asd/', 'root_path': '',
        # 'headers': [(b'host', b'localhost'), (b'connection', b'upgrade'), (b'upgrade', b'websocket'), (b'sec-websocket-version', b'13'), (b'sec-websocket-key', b'qqONMmXfaGW4A1nxqSyViQ=='), (b'sec-websocket-extensions', b'permessage-deflate; client_max_window_bits')], 'query_string': b'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoic29ja2V0IiwiZXhwIjoxNzQ2OTk5NDcyLCJpYXQiOjE3NDY5OTk0NjIsImp0aSI6ImY0ZjIyNmFkYzU1MzQxOWM4MzBhMzMzMDY2NDE3YzBkIiwidXNlcl9pZCI6N30.5pBXqLHEO2N11Yinv39eT0qyzyp3fMQsSBk3H-X0dqY', 'client': ['172.18.0.2', 59110], 'server': ['172.18.0.6', 8000], 'subprotocols': [], 'asgi': {'version': '3.0'}, 'user': <UserModel: user2@gmail.com>, 'path_remaining': '',
        # 'url_route': {'args': (), 'kwargs': {'room': 'asd'}}}
        self.room_name = self.scope['url_route']['kwargs']['room']
        self.user_name = await self.get_profile_name()

    # we need to do as async, 'cause we want to retrieve 'profile' from db
    @database_sync_to_async
    def get_profile_name(self):
        user = self.scope['user']
        return user.profile.name