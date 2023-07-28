from django.urls import path
from .views import FieldList, BookingList, BookingDetail, FieldAvailability

urlpatterns = [
    path('fields/', FieldList.as_view(), name='field-list'),
    path('bookings/', BookingList.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='booking-detail'),
    path('field_availability/<int:field_id>/', FieldAvailability.as_view(), name='field-availability'),
]
