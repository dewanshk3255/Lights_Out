# Generated by Django 3.1 on 2020-09-04 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_auto_20200904_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]