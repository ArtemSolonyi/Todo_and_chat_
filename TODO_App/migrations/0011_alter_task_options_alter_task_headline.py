# Generated by Django 4.0.1 on 2022-01-22 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_App', '0010_alter_task_headline'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterField(
            model_name='task',
            name='headline',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
