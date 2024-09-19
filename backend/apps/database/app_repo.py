"""Contains the app repository."""

from logging import getLogger

from apps.database.interfaces.app_repo import IApplicationRepository
from apps.models import HomePortalApplication, HomePortalCategory


class ApplicationRepository(IApplicationRepository):
    """Application repository."""

    log = getLogger(__name__)

    def __init__(self) -> None:
        """Initialize the repository."""
        self.log.info("Application repository initialized.")

    async def get_applications(self) -> list[HomePortalApplication]:
        """
        Get all the applications.

        Returns:
            list[HomePortalApplication]: All the applications.
        """
        result = HomePortalApplication.objects.all()
        all_apps = [app async for app in result]
        return all_apps

    async def get_nav_menu_items(self) -> list[HomePortalApplication]:
        """
        Get all nav menu items.

        Returns:
            list[HomePortalApplication]: All the side menu applications.
        """
        result = HomePortalApplication.objects.filter(nav_link_visible=True)
        nav_menu_apps = [app async for app in result]
        return nav_menu_apps

    async def get_side_menu_items(self) -> list[HomePortalApplication]:
        """
        Get all side menu items.

        Returns:
            list[HomePortalApplication]: All the side menu applications.
        """
        result = HomePortalApplication.objects.filter(side_menu_visible=True).select_related(
            "category"
        )
        nav_menu_apps = [app async for app in result]
        return nav_menu_apps

    async def get_categories(self) -> list[HomePortalCategory]:
        """
        Get all side menu categories.

        Returns:
            list[HomePortalCategory]: All the side menu categories.
        """
        result = HomePortalCategory.objects.all()
        categories = [app async for app in result]
        return categories
