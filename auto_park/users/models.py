from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):

    def create(self, **kwargs):
        password = kwargs.get("password")
        if password is not None:
            kwargs['password'] = make_password(password)
        return super().create(**kwargs)

    def create_user(self, phone_number, password, **kwargs):
        if not phone_number:
            raise AttributeError("User email not specified")

        phone_number = self.normalize_email(phone_number)
        user = self.model(phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **kwargs):

        kwargs.update(
            {
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            }
        )
        return self.create_user(phone_number, password, **kwargs)


class User(AbstractUser):

    phone_number = models.CharField("Phone number", max_length=15, unique=True)

    username = None
    first_name = None
    last_name = None


    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email