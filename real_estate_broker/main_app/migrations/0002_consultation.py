# Generated by Django 4.2.9 on 2024-12-22 10:00

from django.db import migrations, models
import real_estate_broker.main_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100, validators=[real_estate_broker.main_app.validators.IsItAPhoneNumber()])),
                ('choices', models.CharField(choices=[('Инвестиции', 'Инвестиции'), ('Индивидуална стратегия за твоя бизнес', 'Индивидуална стратегия за твоя бизнес'), ('Недвижими имоти', 'Недвижими имоти')], max_length=100)),
                ('consultation_datetime', models.DateTimeField(validators=[real_estate_broker.main_app.validators.DateChecker()])),
            ],
        ),
    ]
