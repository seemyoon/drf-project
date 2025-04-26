import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.services.jwt_service import ActionToken, ActivateToken, JWTService


class EmailService:
    @classmethod  # Make a class method (cls instead of self) so that you can call the method without creating an object of this class.
    def __send_email(cls, to: str, tempalate_name: str, context: dict, subject: str) -> None:
        # to: who to send the email to
        # tempalate_name: path to HTML template
        # context: data to substitute into template
        # subject: email subject

        template = get_template(tempalate_name)
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
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost/activate/{token}'
        cls.__send_email(
            to=user.email,
            tempalate_name='register.html',
            context={'name': user.profile.name, 'url': url},
            subject='Register'
        )
