# Generated by Django 5.1.7 on 2025-04-05 00:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usermodel_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(150)]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z][a-z]{,19}$', 'Only alpha characters are allowed')]),
        ),
    ]
