from rest_framework import generics
from .models import User
from .serial import UserSerial

class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerial