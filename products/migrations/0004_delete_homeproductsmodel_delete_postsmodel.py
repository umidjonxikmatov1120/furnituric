# Generated by Django 5.0 on 2023-12-21 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_postsmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomeProductsModel',
        ),
        migrations.DeleteModel(
            name='PostsModel',
        ),
    ]