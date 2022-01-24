from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerialzer, AuthTokenSerializer

# Create your views here.


class CreateUserView(CreateAPIView):
    """Create new user"""

    serializer_class = UserSerialzer


class CreateTokenView(ObtainAuthToken):
    """Create new auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
