# Generated by Django 3.2.13 on 2022-06-10 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
