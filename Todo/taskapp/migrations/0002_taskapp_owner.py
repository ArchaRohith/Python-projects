# Generated by Django 4.2.11 on 2024-04-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskapp',
            name='owner',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
