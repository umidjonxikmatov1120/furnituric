# Generated by Django 5.0 on 2023-12-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_homeproductsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_description', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('is_who', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]