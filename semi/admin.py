from django.contrib import admin
from .models import Seminar, Booking
# Register your models here.


class SeminarAdmin(admin.ModelAdmin):
    list_display = ('id', 'semi_name', 'department', 'teach_name', 'mail', 'area_of_seminar', 'semi_schedule', 'seni_men_num', 'seni_women_num', 'juni_men_num', 'juni_women_num', 'feature', 'semi_update_at', 'account')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_num', 'booking_date')

admin.site.register(Seminar, SeminarAdmin)
admin.site.register(Booking, BookingAdmin)
