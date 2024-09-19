"""Contains the user repository for the project."""

from logging import getLogger

from django.contrib.auth.models import AbstractBaseUser, AnonymousUser, User

from hub.database.interfaces.user_interface import IUserRepo

log = getLogger(__name__)
log.info("HUB user repository loading...")


class UserRepo(IUserRepo):
    """User repository."""

    def __init__(self) -> None:
        """Initialize class."""
        super().__init__()

    def is_user_authenticated(self, user: AbstractBaseUser | AnonymousUser | User) -> bool:
        """
        Check if the user is authenticated.

        Args:
            user (AbstractBaseUser | AnonymousUser | User): The user to check.

        Returns:
            bool: True if the user is authenticated, False otherwise.
        """
        authenticated = user.is_authenticated
        return authenticated


log.info("HUB user repository loaded.")
