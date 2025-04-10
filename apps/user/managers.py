from django.contrib.auth.models import UserManager as Manager


class UserManager(Manager):
    def create_user(
            self, email=None, password=None, **extra_fields
    ):
        if not email:
            raise ValueError('email must be provided')

        if not password:
            raise ValueError('Password must be provided')

        email = self.normalize_email(
            email)  # we do normalize_email, for instance if we need to do normal formate after @ (not an uppercase)
        user = self.model(email=email,
                          **extra_fields)  # a new instance of the model is created, which is not saved in the database, but already contains all the transferred data (in this case, email and any additional fields via **extra_fields).
        user.set_password(password)  # hashing password
        user.save()
        return user

    def create_superuser(
            self, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault('is_active',
                                True)  # setdefault() is a dictionary method in Python that is used to set default values for keys if they do not already exist in the dictionary. If the key already exists in the dictionary, its value will not be changed.
        # Temporary blocking: for example, if the account needs to be verified or is awaiting approval.
        # Blocking on request: if the administrator decides that the user should no longer have access to the system, but does not delete their data.

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields['is_staff'] is not True:
            raise ValueError('Superuser must be is_staff')

        if extra_fields['is_active'] is not True:
            raise ValueError('Superuser must be is_active')

        if extra_fields['is_superuser'] is not True:
            raise ValueError('Superuser must be is_superuser')

        user = self.create_user(email=email, password=password, **extra_fields)
        # extra_fields is an additional parameter that allows you to pass custom fields when creating a user. These fields do not necessarily have to be specified in the method (e.g.username,email, password), but can be useful for passing additional data such as is_active, is_staff, is_superuser and other custom attributes.
        return user
