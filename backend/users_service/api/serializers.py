"""
A module that contains serializers of the users package.

Classes:
    - `UserSerializer`: A class that serializer the AuthUser model.
"""

from rest_framework import serializers

from .models import AuthUser


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the AuthUser model.

    Attributes:
        password: The password of the user and it is written only

    Methods:
        - `validate_password(password)`: A method to validate the user password when registering
    """

    password: serializers.CharField = serializers.CharField(write_only=True)

    class Meta:
        """Metaclass for UserSerializer.

        Attributes:
            model: The AuthUser model
            fields: A list of AuthUser fields that need to be serialized
        """

        model: AuthUser = AuthUser
        fields: list[str] = [
            "user_id",
            "email",
            "username",
            "password",
            "created_at",
            "updated_at",
        ]

    def validate_password(self, password: str) -> str:
        """Validate the entered password.

        Args:
            password: The password entered by the user.

        Raises:
            serializers.ValidationError: If the password is less than 8 characters.

        Returns:
            The validated password.

        """
        if len(password) < 8:
            raise serializers.ValidationError("Password must be more than 8 characters!")
        return password
