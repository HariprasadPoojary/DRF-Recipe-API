from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer


class UserSerialzer(ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ("email", "password", "name")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 5,
            }
        }

    def create(self, validated_data):
        """Create new user with encrypted password and return the same"""
        return get_user_model().objects.create_user(**validated_data)
