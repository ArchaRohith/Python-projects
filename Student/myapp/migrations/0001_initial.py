# Generated by Django 4.2.11 on 2024-04-08 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=200)),
                ('coursename', models.CharField(max_length=200)),
                ('fees', models.PositiveIntegerField()),
            ],
        ),
    ]
