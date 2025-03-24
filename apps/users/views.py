from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.request import Request

from apps.users.filter import filter_users
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserListCreateView(GenericAPIView, ListModelMixin,
                         CreateModelMixin):  # GenericAPIView inherit from APIView, but have more functionality
    # we can delete queryset = UserModel.objects.all(), because we specified in filter.py file
    serializer_class = UserSerializer

    def get_queryset(self):  # give ability to specified queryset
        # return super().get_queryset() # we don't use it
        request: Request = self.request
        return filter_users(request.query_params)

    def get(self, request: Request, *args,
            **kwargs):
        """"
        description
        1. about objects.all()
        users = UserModel.objects.all()  # it's queryset - return query, not from DB.
        print(users.query) # evidence that confirms this, that queryset return query
        2. filter
        users.filter(weight=)  # cover of our model. roughly speaking is query.
        example of .filter: weight=, name__exact=, name__endswith=,  status__isnull=(if set 'i'- does not pay attention to case)
        .filter can be a lot, for example:
        users.filter(name__endswith=)
        users.filter(name__endswith=)
        users.filter(weight=)
        3.| and &
        from django.db.models import Q - ability specified "or" (|) "and" (&)
        users = users.filter(Q(weight__gt=55) | Q(name='asd'))
        | is mean we filter weight__gt=20 or name='alex';
        & is mean we filter weight__gt=20 and name='alex';
        if we start use Q, and we should continue use it
        4.exclude()
        exclude() - exclude smth from request:
        users = UserModel.objects.filter(Q(weight=65) | Q(name='alex')).exclude(status=True)
        5.order_by()
        order_by() - sort by smth from smallest to biggest:
        users = UserModel.objects.filter(Q(weight=65) | Q(name='alex')).exclude(status=True).order_by('weight')
        order_by() - sort by smth from biggest to smallest (we set minus '-'):
        users = UserModel.objects.filter(Q(weight=65) | Q(name='alex')).exclude(status=True).order_by('-weight')
        if we have the same value, we can add the second parameter:
        -||-.order_by('weight', 'age')
        5.reverse()
        6.[one_value:second_value]
        limit from first to the last value
        [one_value:second_value:third_value]
        third_value, for instance [5:10:2] - step (select every second element).
        7.values()
        users = UserModel.objects.all().values('id','name','price')
        we choose particular fields need for me.
        8. aggregate functions:
        Min and Max from django models
        aggregate = UserModel.objects.aggregate(Min('size'), Max('size'))
        9. annotate():
        used to aggregate data. Used to add calculated fields.
        Count from django models
        We give count (lower letter) field a name ourselves
        example:
        annotate = UserModel.objects.values('name').annotate(count=Count('name'))
        """

        return super().list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class UserRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    qs = UserModel.objects.all()  # it's necessary for GenericAPIView. we need to specify qs
    serializer_class = UserModel.objects.all()

    # def get(self, *args, **kwargs):
    #     # we use GenericAPIView we may not avoid the following code:
    #     # pk = kwargs['pk']
    #     # try:
    #     #     user = UserModel.objects.get(pk=pk)
    #     #
    #     # except UserModel.DoesNotExist:
    #     #     return Response(f'User {pk} does not exist', status.HTTP_404_NOT_FOUND)
    #     # modified version:
    #     user = self.get_object()

    #     serializer = UserSerializer(user)
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def put(self, *args, **kwargs):
    #     # the same situation as in get method
    #     user = self.get_object()

    #     data = self.request.data

    # serializer = UserSerializer(user, data, partial=True) # partial=True is mean not all fields must be changed
    #     serializer.is_valid(raise_exception=True)

    #     serializer.save()

    #     return Response(serializer.data, status.HTTP_200_OK)

    # def delete(self, *args, **kwargs):
    #     # the same situation as in get method
    #     self.get_object().delete()

    #     return Response(status.HTTP_204_NO_CONTENT)

    def get(self, request: Request, *args, **kwargs):  # kwargs = {'pk': 5}
        return super().retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def patch(self, request: Request, *args,
              **kwargs):  # METHOD PATCH as partial=True is mean not all fields must be changed.
        # WITH PUT WE NEED TO MODIFY ALL FIELDS
        return super().partial_update(request, *args, **kwargs)

