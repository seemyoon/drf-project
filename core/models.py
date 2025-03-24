from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True # to avoid generating migrations

    created_at = models.DateTimeField(
        auto_now_add=True)  # we have DateTimeField (with time) and DateField (without time) as well
    updated_at = models.DateTimeField(auto_now=True)
