from django.db.models import QuerySet
from django.http import QueryDict

from rest_framework.exceptions import ValidationError

from apps.users.models import UserModel


# filter files need to dynamic catch some different lookups with their values
def filter_users(query: QueryDict) -> QuerySet:
    qs = UserModel.objects.all()

    for k, v in query.items():  # k - lookup; v - value
        match k:
            case 'age__gt':
                qs = qs.filter(age__gt=v)
            case 'age__lt':
                qs = qs.filter(age__lt=v)
            case _:
                raise ValidationError(f'{k} not allowed')

    return qs
