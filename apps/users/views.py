from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.filter import filter_users
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserListCreateView(APIView):
    """"
    APIView
    - Base class for views in DRF.
    requires explicit definition of methods (get, post, put, delete, etc.).
    does not include built-in logic for working with models.

    GenericAPIView. GenericAPIView inherit from APIView
    with it, we can do our code shorter
    inherits from APIView, but adds support for working with models.
    allows the use of queryset, serializer_class, pagination, and filtering.
    more often used as a basis for generic classes (ListAPIView, RetrieveAPIView, etc.).
    """

    def get(self, request: Request, *args,
            **kwargs):  # we indicate request: Request, because it's necessary to catch info query_params. request is the same request as in self, use when only self doesn't work
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

        qs = filter_users(request.query_params)
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = UserSerializer(
            data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            user = UserModel.objects.get(pk=pk)

        except UserModel.DoesNotExist:
            return Response(f'User {pk} does not exist', status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            user = UserModel.objects.get(pk=pk)

        except UserModel.DoesNotExist:
            return Response(f'User {pk} does not exist', status.HTTP_404_NOT_FOUND)

        data = self.request.data

        serializer = UserSerializer(user, data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            UserModel.objects.get(pk=pk).delete()
        except UserModel.DoesNotExist:
            return Response(f" User {pk} does not exist", status.HTTP_404_NOT_FOUND)
        return Response(status.HTTP_204_NO_CONTENT)
