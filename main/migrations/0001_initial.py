# Generated by Django 4.0.1 on 2022-01-16 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models
import themvu.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50, verbose_name='Nomi (uz)')),
                ('name_en', models.CharField(max_length=50, verbose_name='Nomi (en)')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
            bases=(themvu.mixins.TranslateMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_uz', models.CharField(max_length=100, verbose_name='Sarlavha (uz)')),
                ('subject_en', models.CharField(max_length=100, verbose_name='Sarlavha (en)')),
                ('video', models.FileField(upload_to=main.models.posts_upload_to, verbose_name='Video')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('view', models.IntegerField(default=0)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='main.category')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(themvu.mixins.TranslateMixin, models.Model),
        ),
    ]
