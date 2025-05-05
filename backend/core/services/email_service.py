import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from configs.celery import app
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

UserModel = get_user_model()


class EmailService:
    @staticmethod
    @app.task  # task for celery. when celery starts it will consider all functions and methods that are marked with this decorator and will consider them as its tasks
    def __send_email(to: str, template_name: str, context: dict, subject: str) -> None:
        # to: who to send the email to
        # template_name: path to HTML template
        # context: data to substitute into template
        # subject: email subject

        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(
            to=[to],
            from_email=os.environ.get('EMAIL_HOST_USER'),
            subject=subject
        )
        msg.attach_alternative(html_content, 'text/html')
        # Attach HTML version of the email (alternative version for HTML-supporting clients).
        msg.send()

    @classmethod
    def register(cls, user):
        # Even if __send_email became @staticmethod, it does not prevent it from being called via cls.__send_email
        # register and recovery use cls.__send_email because they want to be independent of the specific class name and support extensibility.
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost/activate/{token}'
        cls.__send_email.delay(
            # we don't specify .delay, nothing will happen. and celery don't work here
            to=user.email,
            template_name='register.html',
            context={'name': user.profile.name, 'url': url},
            subject='Register'
        )

    @classmethod
    def recovery(cls, user):
        token = JWTService.create_token(user, RecoveryToken)
        url = f'http://localhost/auth/recovery/{token}'
        cls.__send_email(
            to=user.email,
            template_name='recover_password.html',
            context={'name': user.profile.name, 'url': url},
            subject='Recovery'
        )

    @staticmethod
    @app.task
    def spam():
        for user in UserModel.objects.all():
            EmailService.__send_email(
                to=user.email,
                template_name='spam.html',
                context={},
                subject='SPAM')
