from django import forms
from .models import Seminar, Booking


class SeminarForm(forms.ModelForm):
    class Meta:
        model = Seminar
        fields = ['semi_name', 'mail', 'area_of_seminar', 'semi_schedule', 'seni_men_num', 'seni_women_num', 'juni_men_num', 'juni_women_num', 'feature', 'visitable_date', 'on_offline', 'message_for_sutudent', 'semi_image1', 'semi_image2', 'semi_image3', 'semi_image4', 'semi_image5', 'semi_image6']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['semi_image1'].required = False
        self.fields['semi_image2'].required = False
        self.fields['semi_image3'].required = False
        self.fields['semi_image4'].required = False
        self.fields['semi_image5'].required = False
        self.fields['semi_image6'].required = False


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['stu_num', 'booking_date', 'select_semi']
