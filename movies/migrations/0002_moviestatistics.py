# Generated by Django 5.1.1 on 2024-11-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_movies', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
