from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static


class User(AbstractUser):
    photo = models.ImageField(upload_to='profile')

    @property
    def avatar(self):
        if self.photo:
            return self.photo.url

        return static("img/no-photo.jpg")
