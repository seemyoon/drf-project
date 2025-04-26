from typing import Type

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from core.enums.action_token_enum import ActionTokenEnum
from core.exceptions.jwt_exception import JWTException
from rest_framework_simplejwt.tokens import BlacklistMixin, Token

ActionTokenClassType = Type[BlacklistMixin | Token]  # own typing to easy work

UserModel = get_user_model()


# BlacklistMixin need for token_blacklist_blacklistedtoken
# Token is base token

class ActionToken(BlacklistMixin, Token):
    pass


class ActivateToken(ActionToken):
    token_type = ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.lifetime


class JWTService:
    # one method create token
    @staticmethod
    def create_token(user, token_class: ActionTokenClassType):  # generate token for particular user
        return token_class.for_user(user)

    # second method verify token
    @staticmethod
    def verify_token(token, token_class: ActionTokenClassType):  # !verify the same class, which we used for generation
        try:
            token_res = token_class(token)
            token_res.check_blacklist()  # check if token is in token_blacklist or not
        except Exception:
            raise JWTException

        token_res.blacklist()  # if everything ok, we pass valid token to blacklist
        user_id = token_res.payload.get('user_id')
        # we can find user via model, but there is a method in django, which makes it easier
        return get_object_or_404(UserModel, pk=user_id)
