"""
A module that contains models of the users package.

Classes:
    - `AuthUser`: A class that creating user model.
"""

from uuid import uuid4

from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.db import models

from .jwt_auth import generate_token


class AuthUser(models.Model):
    """Model for authenticated users.

    Attributes:
        user_id: id of the user
        email: the email of the user
        username: the username of the user
        password: the password of the user
        token: the token of the user
        created_at: the datetime when user is created
        updated_at: the updated datatime when updating the user

    Methods:
        - `set_password(raw_password)`: A method to set user password to hash password
        - `check_password(new_password)`: A method to check if the password is correct or not
        - `set_token(email)`: A method to set user token
    """

    class Meta:
        """Metaclass for AuthUser model.

        Attributes:
            db_table: the table name
        """

        db_table: str = "api_auth_users"

    user_id: models.UUIDField = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)

    email: models.EmailField = models.EmailField(max_length=255, db_index=True, null=False, blank=False, unique=True)
    username: models.CharField = models.CharField(max_length=50, db_index=True, null=False, blank=False, unique=True)
    password: models.CharField = models.CharField(max_length=255, null=False, blank=False)
    token: models.CharField = models.CharField(max_length=255, null=True, blank=True)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True, null=True)

    def set_password(self, raw_password: str) -> None:
        """Set password for the user.

        Args:
            raw_password: The raw password entered by the user.
        """
        self.password = make_password(raw_password)

    def check_password(self, new_password: str) -> bool:
        """Check if the entered password is correct.

        Args:
            new_password: The new password entered by the user.

        Returns:
            True if the password is correct, else False.
        """
        return check_password(new_password, self.password)

    def set_token(self, email: str) -> None:
        """Generate and set token for the user.

        Args:
            email: Email of the user.
        """
        self.token = generate_token(email, settings.SECRET_KEY)
