# Generated by Django 4.2.9 on 2025-01-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_event_location_event_organizer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заглавие')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image_url', models.URLField(max_length=500, verbose_name='URL на изображението')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата на създаване')),
            ],
        ),
    ]
