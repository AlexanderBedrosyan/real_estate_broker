# Generated by Django 4.2.9 on 2024-12-20 14:27

from django.db import migrations, models
import real_estate_broker.main_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(validators=[real_estate_broker.main_app.validators.IsItAPhoneNumber()]),
        ),
    ]
