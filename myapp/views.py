from rest_framework.response import Response
from rest_framework.views import APIView


# APIView the lowest file to inherit
# Response - answer for client request

class MyAppView(APIView):
    def get(self, *args, **kwargs):
        # print(self.request.query_params)  # catch params
        # print(self.request.query_params.dict())  # catch params in dict format

        return Response('hello from get')

    def post(self, *args, **kwargs):
        print(self.request.data)  # as body from client

        return Response('hello from post')

    def put(self, *args, **kwargs):
        return Response('hello from put')

    def patch(self, *args, **kwargs):
        return Response('hello from patch')

    def delete(self, *args, **kwargs):
        return Response('hello from delete')


class MySecondAppView(APIView):
    def get(self, *args, **kwargs):
        print(kwargs)  # catch params from path('mysecondapp/<int:age>', MySecondAppView.as_view() )

        # return Response('hello from get in second view')
        return Response(kwargs['age'])  # return response
