"""Contains the app service."""

from logging import getLogger

from apps.database.app_repo import ApplicationRepository
from apps.models import HomePortalApplication
from apps.schemas.output import (
    ApplicationSchema,
    NavMenuApplicationSchema,
    SideMenuApplicationSchema,
    SideMenuApplicationsSchema,
    SideMenuCategorySchema,
)
from apps.services.interfaces.app_service import IApplicationService


class ApplicationService(IApplicationService):
    """Application service."""

    log = getLogger(__name__)
    repository = ApplicationRepository()

    def __init__(self) -> None:
        """Initialize the service."""
        self.log.info("Application service initialized.")

    async def get_applications(self) -> list[ApplicationSchema]:
        """
        Get all the applications.

        Returns:
            list[ApplicationSchema]: All the applications.
        """
        self.log.info("Getting all applications.")
        result = await self.repository.get_applications()
        apps = [ApplicationSchema.from_orm(app) for app in result]
        return apps

    async def get_nav_menu_applications(self) -> list[NavMenuApplicationSchema]:
        """
        Get all nav menu applications.

        Returns:
            list[NavMenuApplicationSchema]: All the nav menu applications.
        """
        self.log.info("Getting all nav menu applications.")
        result = await self.repository.get_nav_menu_items()
        nav_menu_apps = [NavMenuApplicationSchema.from_orm(app) for app in result]
        return nav_menu_apps

    async def get_side_menu_applications(self) -> SideMenuApplicationsSchema:
        """
        Get all side menu applications.

        Returns:
            list[SideMenuCategorySchema]: All the nav menu applications.
        """
        self.log.info("Getting all side menu applications.")
        categories = await self.repository.get_categories()
        side_menu_apps = await self.repository.get_side_menu_items()
        apps_with_category: list[HomePortalApplication] = []

        result = SideMenuApplicationsSchema(categories=[], no_category=[])

        for app in side_menu_apps:
            if app.category is None:
                result.no_category.append(SideMenuApplicationSchema.from_orm(app))
            else:
                apps_with_category.append(app)

        for category in categories:
            corresponding_apps = [
                SideMenuApplicationSchema.from_orm(app)
                for app in apps_with_category
                if app.category and app.category.id == category.id
            ]
            result.categories.append(
                SideMenuCategorySchema(
                    category=category.title, icon=category.icon, applications=corresponding_apps
                )
            )

        return result
