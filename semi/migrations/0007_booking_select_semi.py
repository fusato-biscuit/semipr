# Generated by Django 2.0.2 on 2020-11-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi', '0006_auto_20201113_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='select_semi',
            field=models.IntegerField(choices=[(1, '未選択'), (2, '井端ゼミ'), (3, '井村ゼミ'), (4, '上江洲ゼミ'), (5, '熊谷ゼミ'), (6, '小西ゼミ'), (7, '清水ゼミ'), (8, '末崎ゼミ'), (9, '伊達ゼミ'), (10, '田中ゼミ'), (11, '中野ゼミ'), (12, '西迫ゼミ'), (13, '比屋定ゼミ'), (14, '前津ゼミ'), (15, '山下ゼミ')], default=1),
        ),
    ]
