# Generated by Django 4.0.1 on 2022-01-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=100, verbose_name='Почта'),
            preserve_default=False,
        ),
    ]