"""Contains the app repository."""

from abc import ABC, abstractmethod

from apps.models import HomePortalApplication, HomePortalCategory


class IApplicationRepository(ABC):
    """Application repository."""

    @abstractmethod
    async def get_applications(self) -> list[HomePortalApplication]:
        """
        Get all the applications.

        Returns:
            list[HomePortalApplication]: All the applications.
        """

    @abstractmethod
    async def get_nav_menu_items(self) -> list[HomePortalApplication]:
        """
        Get all nav menu items.

        Returns:
            list[HomePortalApplication]: All the side menu applications.
        """

    @abstractmethod
    async def get_side_menu_items(self) -> list[HomePortalApplication]:
        """
        Get all side menu items.

        Returns:
            list[HomePortalApplication]: All the side menu applications.
        """

    @abstractmethod
    async def get_categories(self) -> list[HomePortalCategory]:
        """
        Get all side menu categories.

        Returns:
            list[HomePortalCategory]: All the side menu categories.
        """
