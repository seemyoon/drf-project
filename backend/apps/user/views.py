import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives  # to sent letters
from django.template.loader import get_template  # load html templates

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.user.serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()  # we can not refer the user model as we did with other models (because of troubles with django)
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class BlockUserView(GenericAPIView):
    def get_queryset(self):
        return UserModel.objects.all().exclude(id=self.request.user.id)

    # The get_queryset method is needed to exclude the current user from the selection.
    #
    # Without it, self.get_object() could return itself.
    # With it, you can't block yourself.
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()

        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status.HTTP_200_OK)


class UnBlockUserView(GenericAPIView):
    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()

        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status.HTTP_200_OK)


class UserUpdateIsStaffView(GenericAPIView):
    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_active = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class SendEmailTestView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        template = get_template('test_email.html')
        html_content = template.render({'name': 'Sasha'})  # then we need to render this template to content
        # as args we can pass smth dynamically in <h2>hello from {{ name }} drf-project!</h2>
        msg = EmailMultiAlternatives(
            subject='Test Email',
            from_email=os.environ.get('EMAIL_HOST_USER'),
            to=['alejandrosdeveloper@gmail.com']  # we can set several recipients
        )

        msg.attach_alternative(html_content, 'text/html')
        # with this we can add to our msg
        msg.send()
        return Response({'message': 'Email sent!'}, status.HTTP_200_OK)
