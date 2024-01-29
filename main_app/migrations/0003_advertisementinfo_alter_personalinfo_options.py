# Generated by Django 4.2.9 on 2024-01-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_personalinfo_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('video', models.ImageField(blank=True, null=True, upload_to='static/images')),
            ],
            options={
                'verbose_name': 'FP Adv Information',
                'verbose_name_plural': 'FP Adv Information',
            },
        ),
        migrations.AlterModelOptions(
            name='personalinfo',
            options={'verbose_name': 'FP Personal Information', 'verbose_name_plural': 'FP Personal Information'},
        ),
    ]
