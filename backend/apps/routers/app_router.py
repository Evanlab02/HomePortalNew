"""Contains the application router."""

from django.http import HttpRequest
from ninja import Router

from apps.schemas.output import (
    ApplicationsSchema,
    NavMenuApplicationsSchema,
    SideMenuApplicationsSchema,
)
from apps.services.app_service import ApplicationService
from hub.auth.session_auth import SessionAuth

session_auth = SessionAuth()
app_router = Router(auth=session_auth, tags=["Applications"])
app_service = ApplicationService()


@app_router.get("", response={200: ApplicationsSchema})
async def get_applications(request: HttpRequest) -> ApplicationsSchema:
    """
    Get all the applications.

    Returns:
        ApplicationsSchema: All the applications.
    """
    apps = await app_service.get_applications()
    return ApplicationsSchema(applications=apps)


@app_router.get("/navmenu", response={200: NavMenuApplicationsSchema})
async def get_nav_menu_applications(request: HttpRequest) -> NavMenuApplicationsSchema:
    """
    Get all the nav menu applications.

    Returns:
        NavMenuApplicationsSchema: All the nav menu applications.
    """
    apps = await app_service.get_nav_menu_applications()
    return NavMenuApplicationsSchema(applications=apps)


@app_router.get("/sidemenu", response={200: SideMenuApplicationsSchema})
async def get_side_menu_applications(request: HttpRequest) -> SideMenuApplicationsSchema:
    """
    Get all the side menu applications.

    Returns:
        SideMenuApplicationsSchema: All the side menu applications.
    """
    return await app_service.get_side_menu_applications()
