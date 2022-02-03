# Generated by Django 4.0.1 on 2022-01-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_App', '0002_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=30, verbose_name='Имя'),
            preserve_default=False,
        ),
    ]
