"""Contains the app service interface."""

from abc import ABC, abstractmethod

from apps.schemas.output import (
    ApplicationSchema,
    NavMenuApplicationSchema,
    SideMenuApplicationsSchema,
)


class IApplicationService(ABC):
    """Application service."""

    @abstractmethod
    async def get_applications(self) -> list[ApplicationSchema]:
        """
        Get all the applications.

        Returns:
            list[ApplicationSchema]: All the applications.
        """

    @abstractmethod
    async def get_nav_menu_applications(self) -> list[NavMenuApplicationSchema]:
        """
        Get all nav menu applications.

        Returns:
            list[NavMenuApplicationSchema]: All the nav menu applications.
        """

    @abstractmethod
    async def get_side_menu_applications(self) -> SideMenuApplicationsSchema:
        """
        Get all side menu applications.

        Returns:
            list[SideMenuCategorySchema]: All the nav menu applications.
        """
