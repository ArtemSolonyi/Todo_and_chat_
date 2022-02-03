# Generated by Django 4.0.1 on 2022-01-22 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_App', '0008_remove_task_descrpition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name_user_articles',
        ),
        migrations.AddField(
            model_name='task',
            name='name_user_articles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TODO_App.user'),
        ),
    ]
