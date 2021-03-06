# Generated by Django 2.0.2 on 2020-11-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi', '0011_auto_20201122_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='select_semi',
            field=models.IntegerField(choices=[(1, '未選択'), (2, '井端ゼミ(法律)'), (3, '井村ゼミ(法律)'), (4, '上江洲ゼミ(法律)'), (5, '上江洲ゼミ(地行)'), (6, '熊谷ゼミ(法律)'), (7, '熊谷ゼミ(地行)'), (8, '黒柳ゼミ(地行)'), (9, '小西ゼミ(法律)'), (10, '小西ゼミ(地行)'), (11, '佐藤ゼミ1(地行)'), (12, '佐藤ゼミ2(地行)'), (13, '芝田ゼミ(地行)'), (14, '柴田ゼミ(地行)'), (15, '清水ゼミ(法律)'), (16, '末崎ゼミ(法律)'), (17, '平ゼミ(地行)'), (18, '伊達ゼミ(法律)'), (19, '田中ゼミ(法律)'), (20, '田中ゼミ(地行)'), (21, '中野ゼミ(法律)'), (22, '中野ゼミ(地行)'), (23, '西迫ゼミ(法律)'), (24, '野添ゼミ(地行)'), (25, '比屋定ゼミ(法律)'), (26, '比屋定ゼミ(地行)'), (27, '前津ゼミ(法律)'), (28, '前津ゼミ(地行)'), (29, '山下ゼミ(法律)')], default=4),
        ),
    ]
