from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import authentication, permissions

from user.serializers import UserSerialzer, AuthTokenSerializer

# Create your views here.


class CreateUserView(CreateAPIView):
    """Create new user"""

    serializer_class = UserSerialzer


class CreateTokenView(ObtainAuthToken):
    """Create new auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerialzer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
