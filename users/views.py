from rest_framework.views import APIView


class UserListCreateView(APIView):  # create users list
    def post(self, *args, **kwargs):
        data = self.request.data  # body



class UserRetrieveUpdateDestroyView(APIView):  # show users list
    pass
