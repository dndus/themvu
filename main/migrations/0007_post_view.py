# Generated by Django 4.0.1 on 2022-01-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
