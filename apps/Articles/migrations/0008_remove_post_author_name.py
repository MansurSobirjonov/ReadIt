# Generated by Django 3.2.13 on 2022-06-11 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0007_auto_20220611_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_name',
        ),
    ]