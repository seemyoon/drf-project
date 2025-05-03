from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


# This handlers will run before standard handler (like validation handler) in python
def error_handler(exc: Exception,
                  context: dict):  # exc - type of exception, context - info about an error or smth like that.
    handlers = {
        'JWTException': _jwt_validation_exception_handler
        # _jwt_validation_exception_handler (key) - func, which return response
        # don't run _jwt_validation_exception_handler, 'cause we run here: handlers[exc_class](exc, context)

    }
    # we can describe our custom exceptions in 'handlers', e.g 'JWTException'

    response = exception_handler(exc, context)  # response - this response return django

    exc_class = exc.__class__.__name__  # retrieve name of exception

    if exc_class in handlers:
        return handlers[exc_class](exc, context)

    return response  # return response if we don't have handlers like


def _jwt_validation_exception_handler(exc, context):
    return Response({'detail': 'JWT expired or invalid'}, status.HTTP_401_UNAUTHORIZED )
