# view for connecting sockets
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer


class ChatConsumer(GenericAsyncAPIConsumer):
    async def connect(self):
        return await super().connect() # it call 'accept', which accepts connection