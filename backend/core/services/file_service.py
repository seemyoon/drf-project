import os
from uuid import uuid1


def upload_pizza_photo(instance, filename):
    # instance is the model object for which the load function is called.
    ext = filename.split('.')[-1] # retrieve extension
    # return f"photos/{filename}"
    return os.path.join(instance.pizza_shop.name, f"{uuid1()}.{ext}")