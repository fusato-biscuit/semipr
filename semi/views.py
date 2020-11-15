from django.shortcuts import render, redirect, get_object_or_404
from .models import Seminar, Booking
from .forms import SeminarForm, BookingForm


# Create your views here.
def entrance(request):
    return render(request, 'semi/entrance.html')

def seminar(request):
    seminars = Seminar.objects.all()
    return render(request, 'semi/seminar.html', {'seminars': seminars})


def create_seminar(request):
    now_login_user = request.user
    if request.method == 'POST':
        form = SeminarForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.account = now_login_user
            form.save()
            return redirect('semi:seminar')
    else:
        form = SeminarForm()
        return render(request, 'semi/create_seminar.html', {'form': form})


def edit_seminar(request, semi_id):
    edit_semi = get_object_or_404(Seminar, id=semi_id)
    if request.method == "POST":
        form = SeminarForm(request.POST, request.FILES, instance=edit_semi)
        if form.is_valid():
            form.save()
            return redirect('semi:seminar')
    else:
        form = SeminarForm(instance=edit_semi)
    return render(request, 'semi/edit_seminar.html', {'edit_semi': edit_semi, 'form': form})


def detail_seminar(request, semi_id):
    detail_semi = get_object_or_404(Seminar, id=semi_id)
    total_num = detail_semi.seni_men_num + detail_semi.seni_women_num + detail_semi.juni_men_num + detail_semi.juni_women_num
    senior_num = detail_semi.seni_men_num + detail_semi.seni_women_num
    junior_num = detail_semi.juni_men_num + detail_semi.juni_women_num
    return render(request, 'semi/detail_seminar.html', {'detail_semi': detail_semi, 'total_num': total_num, 'senior_num': senior_num, 'junior_num': junior_num})


def delete_seminar(request, semi_id):
    delete_semi = get_object_or_404(Seminar, id=semi_id)
    delete_semi.delete()
    return redirect('semi:seminar')

# 予約登録
def send_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('semi:check_booking')
    else:
        form = BookingForm()
    return render(request, 'semi/send_booking.html', {'form':form})

def check_booking(request):
    return render(request, 'semi/check_booking.html')

# 予約確認
def booking_list(request):
    if request.user.username == 'ibata':
        bookings = Booking.objects.filter(select_semi=2)
    elif request.user.username == 'imura':
        bookings = Booking.objects.filter(select_semi=3)
    elif request.user.username == 'wellgab8':
        bookings = Booking.objects.filter(select_semi=4)
    elif request.user.username == 'kumagaya':
        bookings = Booking.objects.filter(select_semi=5)
    elif request.user.username == 'konisi':
        bookings = Booking.objects.filter(select_semi=6)
    elif request.user.username == 'simizu':
        bookings = Booking.objects.filter(select_semi=7)
    elif request.user.username == 'suezaki':
        bookings = Booking.objects.filter(select_semi=8)
    elif request.user.username == 'date':
        bookings = Booking.objects.filter(select_semi=9)
    elif request.user.username == 'tanaka':
        bookings = Booking.objects.filter(select_semi=10)
    elif request.user.username == 'nakano':
        bookings = Booking.objects.filter(select_semi=11)
    elif request.user.username == 'nisisako':
        bookings = Booking.objects.filter(select_semi=12)
    elif request.user.username == 'hiyajou':
        bookings = Booking.objects.filter(select_semi=13)
    elif request.user.username == 'maetu':
        bookings = Booking.objects.filter(select_semi=14)
    elif request.user.username == 'yamasita':
        bookings = Booking.objects.filter(select_semi=15)
    return render(request, 'semi/booking_list.html', {'bookings': bookings})
