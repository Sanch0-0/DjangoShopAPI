from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import RegistrationSerializer, UpdateSerializer
from .models import User


class RegistrationAPIView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {"email":request.data['email']}
        return response


class UpdateProfileAPIView(UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
