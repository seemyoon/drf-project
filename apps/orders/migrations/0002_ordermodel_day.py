# Generated by Django 5.1.7 on 2025-04-04 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='day',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], default='tuesday', max_length=9),
            preserve_default=False,
        ),
    ]
