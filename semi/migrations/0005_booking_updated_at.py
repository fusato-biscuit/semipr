# Generated by Django 2.0.2 on 2020-11-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi', '0004_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
