"""Contains the outbound schemas for the application management."""

from logging import getLogger

from ninja import ModelSchema, Schema

from apps.models import HomePortalApplication

log = getLogger(__name__)
log.info("application management output schemas loading...")


class ApplicationSchema(ModelSchema):
    """Application details schema."""

    class Meta:
        """Meta class."""

        model = HomePortalApplication
        fields = ["title", "description", "link_name", "link"]


class ApplicationsSchema(Schema):
    """Applications schema."""

    applications: list[ApplicationSchema]


class NavMenuApplicationSchema(ModelSchema):
    """Nav menu application details schema."""

    class Meta:
        """Meta class."""

        model = HomePortalApplication
        fields = ["link", "nav_link_name", "nav_link_icon"]


class NavMenuApplicationsSchema(Schema):
    """Nav menu applications schema."""

    applications: list[NavMenuApplicationSchema]


class SideMenuApplicationSchema(ModelSchema):
    """Side menu application detail schema."""

    class Meta:
        """Meta class."""

        model = HomePortalApplication
        fields = ["link", "side_menu_name", "side_menu_icon"]


class SideMenuCategorySchema(Schema):
    """Side menu category collection schema."""

    category: str
    icon: str
    applications: list[SideMenuApplicationSchema]


class SideMenuApplicationsSchema(Schema):
    """Side menu applications schema."""

    categories: list[SideMenuCategorySchema]
    no_category: list[SideMenuApplicationSchema]


log.info("application management output schemas loaded.")
