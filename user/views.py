from rest_framework.generics import CreateAPIView

from user.serializers import UserSerialzer

# Create your views here.


class CreateUserView(CreateAPIView):
    """Create new user"""

    serializer_class = UserSerialzer
