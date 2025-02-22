# Generated by Django 4.2.11 on 2024-03-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('run_time', models.PositiveIntegerField()),
                ('languages', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
    ]
