from django.shortcuts import render
from datetime import timezone, timedelta


# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import FieldModel, BookingModel
from .serializers import FieldModelSerializer, BookingModelSerializer

class FieldList(generics.ListCreateAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldModelSerializer

class BookingList(generics.ListCreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingModelSerializer

class BookingDetail(generics.RetrieveDestroyAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingModelSerializer

class FieldAvailability(generics.ListAPIView):
    serializer_class = BookingModelSerializer

    def get_queryset(self):
        field_id = self.kwargs['field_id']
        field = FieldModel.objects.get(pk=field_id)
        bookings = FieldModel.booking_set.all().order_by('start_time')
        
        available_times = []
        current_time = timezone.now()
        last_end_time = current_time
        
        for booking in bookings:
            if BookingModel.start_time > last_end_time:
                available_times.append({'start_time': last_end_time, 'end_time': booking.start_time})
            last_end_time = BookingModel.end_time
        
        if last_end_time < current_time.replace(second=0, microsecond=0):
            available_times.append({'start_time': current_time.replace(second=0, microsecond=0),
                                    'end_time': current_time.replace(second=0, microsecond=0) + timedelta(hours=1)})
        
        return available_times
