from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'semi'
urlpatterns = [
    # entrance
    path('', views.entrance, name='entrance'),
    # account
    path('login/', auth_views.LoginView.as_view(template_name='semi/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Read
    path('seminar/', views.seminar, name='seminar'),
    path('seminarbb/', views.seminarbb, name='seminarbb'),
    # Create
    path('create_seminar/', views.create_seminar, name='create_seminar'),
    # Edit
    path('edit_seminar/<int:semi_id>/', views.edit_seminar, name='edit_seminar'),
    # Detail
    path('detail_seminar/<int:semi_id>/', views.detail_seminar, name='detail_seminar'),
    # Delete
    path('delete_seminar/<int:semi_id>/', views.delete_seminar, name='delete_seminar'),
    # Info
    path('info/', views.info, name='info'),
    # Booking(student)
    path('send_booking/', views.send_booking, name='send_booking'),
    path('check_booking/', views.check_booking, name='check_booking'),
    # Booking(admin)
    path('booking_list/', views.booking_list, name='booking_list'),

]
