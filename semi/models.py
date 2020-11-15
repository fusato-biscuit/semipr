from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.


class Seminar(models.Model):
    semi_name = models.CharField(null=False, max_length=30)
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
        (2, '井端ゼミ'),
        (3, '井村ゼミ'),
        (4, '上江洲ゼミ'),
        (5, '熊谷ゼミ'),
        (6, '小西ゼミ'),
        (7, '清水ゼミ'),
        (8, '末崎ゼミ'),
        (9, '伊達ゼミ'),
        (10, '田中ゼミ'),
        (11, '中野ゼミ'),
        (12, '西迫ゼミ'),
        (13, '比屋定ゼミ'),
        (14, '前津ゼミ'),
        (15, '山下ゼミ'),
    )
    select_semi = models.IntegerField(choices=select_semi_choice, default=1)
    updated_at = models.DateTimeField(auto_now=True)
