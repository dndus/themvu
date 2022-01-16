import os
import random
from datetime import datetime
from django.db import models
from themvu.mixins import TranslateMixin
from account.models import User
from django.utils.translation import gettext_lazy as _


def upload_to(name):
    def handle(instance, filename):
        ext = os.path.splitext(filename)[1]

        return "{}/{:%Y}/{:%m}/{:%Y-%m-%d-%H-%M-%S}-{}{}".format(
            name,
            datetime.now(),
            datetime.now(),
            datetime.now(),
            random.randint(10000, 99999),
            ext
        )

    return handle


def posts_upload_to(instance, filename):
    return upload_to("posts")(instance, filename)


class Category(TranslateMixin, models.Model):
    translate_attributes = ['name']

    name_uz = models.CharField(max_length=50, verbose_name="Nomi (uz)")
    name_en = models.CharField(max_length=50, verbose_name="Nomi (en)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Post(TranslateMixin, models.Model):
    translate_attributes = ['subject']

    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=None, null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, default=None, null=False)
    subject_uz = models.CharField(max_length=100, verbose_name=_("Sarlavha (uz)"))
    subject_en = models.CharField(max_length=100, verbose_name=_("Sarlavha (en)"))
    video = models.FileField(verbose_name=_("Video"), upload_to=posts_upload_to)
    added_at = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField(default=0)
    # like = models.IntegerField(default=0)
