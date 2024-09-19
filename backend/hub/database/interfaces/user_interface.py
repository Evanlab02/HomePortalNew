"""Contains the abstract class for user repositories."""

from abc import ABC, abstractmethod
from logging import getLogger

from django.contrib.auth.models import AbstractBaseUser, AnonymousUser, User

log = getLogger(__name__)
log.info("HUB user repository interface loading...")


class IUserRepo(ABC):
    """Abstract class for user repository."""

    def __init__(self) -> None:
        """Initialize class."""
        super().__init__()

    @abstractmethod
    def is_user_authenticated(self, user: AbstractBaseUser | AnonymousUser | User) -> bool:
        """
        Check if the user is authenticated.

        Args:
            user (AbstractBaseUser | AnonymousUser | User): The user to check.

        Returns:
            bool: True if the user is authenticated, False otherwise.
        """


log.info("HUB user repository interface loaded.")
