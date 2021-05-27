# Generated by Django 3.1.7 on 2021-05-27 14:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20210527_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='days',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]