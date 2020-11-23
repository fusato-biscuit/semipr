from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.


class Seminar(models.Model):
    semi_name = models.CharField(null=False, max_length=30)
    department_choice = (
        (1, '未選択'),
        (2, '法律学科'),
        (3, '地域行政学科'),
    )
    department = models.IntegerField(choices=department_choice, default=1)
    teach_name = models.CharField(null=True, max_length=30)
    mail = models.EmailField(max_length=100)
    area_of_seminar = models.TextField(max_length=150)
    semi_schedule = models.TextField(blank=True)
    seni_men_num = models.IntegerField()
    seni_women_num = models.IntegerField()
    juni_men_num = models.IntegerField()
    juni_women_num = models.IntegerField()
    feature = models.TextField(blank=True)
    semi_update_at = models.DateTimeField(auto_now=True)
    visitable_date = models.TextField(max_length=50, blank=True)
    on_offline_choice = (
        (1, 'オンライン'),
        (2, '対面'),
        (3, '未定'),
    )
    on_offline = models.IntegerField(choices=on_offline_choice, default=3)
    message_for_sutudent = models.TextField(max_length=100, blank=True)
    semi_image1 = models.ImageField(upload_to='seminar_photos', blank=True, null=True)
    semi_image2 = models.ImageField(upload_to='seminar_photos', blank=True, null=True)
    semi_image3 = models.ImageField(upload_to='seminar_photos', blank=True, null=True)
    semi_image4 = models.ImageField(upload_to='seminar_photos', blank=True, null=True)
    semi_image5 = models.ImageField(upload_to='seminar_photos', blank=True, null=True)
    semi_image6 = models.ImageField(upload_to='seminar_photos', blank=True, null=True)
    account = models.ForeignKey(get_user_model(), default=1, on_delete=models.CASCADE)


    def __str__(self):
        return self.semi_name


class Booking(models.Model):
    stu_num = models.CharField(null=False, max_length=7)
    booking_date = models.TextField(max_length=50)
    select_semi_choice = (
        (1, '未選択'),
        (2, '井端ゼミ(法律)'),
        (3, '井村ゼミ(法律)'),
        (4, '上江洲ゼミ(法律)'),
        (5, '上江洲ゼミ(地行)'),
        (6, '熊谷ゼミ(法律)'),
        (7, '熊谷ゼミ(地行)'),
        (8, '黒柳ゼミ(地行)'),
        (9, '小西ゼミ(法律)'),
        (10, '小西ゼミ(地行)'),
        (11, '佐藤ゼミ1(地行)'),
        (12, '佐藤ゼミ2(地行)'),
        (13, '芝田ゼミ(地行)'),
        (14, '柴田ゼミ(地行)'),
        (15, '清水ゼミ(法律)'),
        (16, '末崎ゼミ(法律)'),
        (17, '平ゼミ(地行)'),
        (18, '伊達ゼミ(法律)'),
        (19, '田中ゼミ(法律)'),
        (20, '田中ゼミ(地行)'),
        (21, '中野ゼミ(法律)'),
        (22, '中野ゼミ(地行)'),
        (23, '西迫ゼミ(法律)'),
        (24, '野添ゼミ(地行)'),
        (25, '比屋定ゼミ(法律)'),
        (26, '比屋定ゼミ(地行)'),
        (27, '前津ゼミ(法律)'),
        (28, '前津ゼミ(地行)'),
        (29, '山下ゼミ(法律)'),
    )
    select_semi = models.IntegerField(choices=select_semi_choice, default=1)
    updated_at = models.DateTimeField(auto_now=True)
