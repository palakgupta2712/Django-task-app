# Generated by Django 3.1 on 2020-09-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200905_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]