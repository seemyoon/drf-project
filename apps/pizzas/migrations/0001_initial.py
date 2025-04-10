# Generated by Django 5.1.7 on 2025-04-10 00:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizza_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z][a-z]{,19}$', 'Only alpha characters are allowed.')])),
                ('size', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('price', models.FloatField()),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('pizza_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='pizza_shop.pizzashopmodel')),
            ],
            options={
                'db_table': 'pizza',
            },
        ),
    ]
