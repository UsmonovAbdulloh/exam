from .models import UserModel
from .serializers import UserModelSerializer
from rest_framework import generics
from .permission import IsOwnerPermission
from field import FieldModel,FieldModelSerializer


class AllCreateUserView(generics.ListCreateAPIView):
    queryset = UserModel.object.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsOwnerPermission)


class DetailUpdateDeleteUserView(generics.RetriveUpdateDestroyAPIView):
    queryset = UserModel.object.all()
    serializer_class =  UserModelSerializer
    permission_classes = (IsOwnerPermission)

class AllUserField(generics.ListAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldModelSerializer
    permission_classes = (IsOwnerPermission)

class UserBronViews(generics.CreateAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldModelSerializer
    permission_classes = (IsOwnerPermission)


class TimeFieldView(generics.ListAPIView):
    serializer_class = FieldModelSerializer
    permission_classes = (IsOwnerPermission)
    def get_time(self):
        unoccupied_time_str = self.request.query_params.get('time', None)
        queryset = FieldModel.objects.filter(first_time__gt=unoccupied_time_str,end_time__lt=unoccupied_time_str)
        return queryset