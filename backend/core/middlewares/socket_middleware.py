# here we describe our own middleware with which we will replace the base middleware one through which we make the connection
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from core.services.jwt_service import JWTService, SocketToken


@database_sync_to_async
def get_user(token: str | None):
    try:
        return JWTService.verify_token(token, SocketToken)
    except (Exception,):
        pass


class AuthSocketMiddleWare(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        # scope === request in regular http
        # scope return dict. this dict have query_string, like - b'token234ohiu256dasd' and we need to catch it (token)
        # b - binary data, and we need to decode it:
        token = dict([item.split('=') for item in scope['query_string'].decode('utf-8').split('&') if item]).get(
            'token', None)
        # query_string === param
        # '.split('&')' - we might have a few param
        # '&' - to separate every param 9 (query_string)
        # 'if item' - if we have item in query_string at all. return empty list []
        # .get('token', None) - if we have no token - None
        # without .get('token', None) result would be like:  {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoic29ja2V0IiwiZXhwIjoxNzQ2OTkzNjUyLCJpYXQiOjE3NDY5OTM2NDIsImp0aSI6IjcxYjk0ZmNlNGRmMDQ0NTA4NTQxMTcxYTJjMWU2N2JhIiwidXNlcl9pZCI6N30.vceGUUTacSfolF8OwVdEUTSJMeCDEXDi3CXhwYpjh-Q'}

        # we write user for token in scope, and then we can retrieve our user

        # sockets work on async/await, and django - asynchronously, and therefore in order to access django we need to make these methods asynchronous.
        # and therefore we need to interpretative from synchronous variants to asynchronous

        scope['user'] = await get_user(token=token)  # and here we have new parameter user
        return await super().__call__(scope, receive, send)
