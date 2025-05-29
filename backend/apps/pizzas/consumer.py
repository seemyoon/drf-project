from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer

from apps.pizzas.models import PizzaModel
from apps.pizzas.serializer import PizzaSerializer


class PizzaConsumer(
    GenericAsyncAPIConsumer):  # this is a special class for working with WebSocket and observing model changes in Django.

    def __init__(self, *args, **kwargs):  # called when an object of this class is created
        self.group = 'pizzas'  # Create a group attribute where we save the string 'pizzas'. This is the name of the group of WebSocket clients to which information will be sent.
        super().__init__(*args,
                         **kwargs)  # Call __init__ on the parent class so that the initialization is complete and correct.

    async def connect(self):  # Define a method that is executed when a client connects via WebSocket.
        if not self.scope['user']:
            return await self.close()  # If the user is not authorized (not in scope['user']), close the connection.

        await self.accept()  # Accept the WebSocket connection.
        await self.channel_layer.group_add(self.group,
                                           self.channel_name)  # Add this WebSocket to the pizzas group so that it receives messages sent to this group.

    @model_observer(PizzaModel,
                    serializer_class=PizzaSerializer)  # This is an observer for the PizzaModel model. It "watches" for changes (create, edit, delete) and automatically sends data to the client via WebSocket.
    async def pizza_model_activity(self, message, action, subscribing_request_ids,
                                   **kwargs):  # when, for example, someone updates a pizza in the database, you don't call it manually - the library itself does it, for example django-channels-rest-framework.
        for request_id in subscribing_request_ids:
            await self.reply(data=message, action=action, request_id=request_id)

    # message — serialized pizza data,
    # action — what happened (create/update/delete),
    # subscribing_request_ids — who subscribed to notifications,

    @action()  # In order to send to the BE. This is a WebSocket method that is called by the client to subscribe to model changes.
    async def subscribe_to_pizza_model_changes(self, request_id,
                                               **kwargs):  # The client calls this method over WebSocket to subscribe to changes.
        await self.pizza_model_activity.subscribe(
            request_id=request_id)  # Remember this request_id. If the PizzaModel changes, call pizza_model_activity and pass the data there.
