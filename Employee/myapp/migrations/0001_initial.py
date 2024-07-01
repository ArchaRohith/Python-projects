# Generated by Django 4.2.11 on 2024-03-31 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('salary', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
