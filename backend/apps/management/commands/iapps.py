"""Initializes the application with all its groups and permissions."""

from typing import Any, no_type_check

from django.core.management.base import BaseCommand

from apps.models import HomePortalApplication, HomePortalCategory


class Command(BaseCommand):
    """Create all base groups and permissions."""

    @no_type_check
    def handle(self, *args: Any, **options: Any) -> None:
        """Create all base groups and permissions."""
        category = HomePortalCategory.objects.create(title="Administration", icon="CodeFilled")
        category.save()

        app = HomePortalApplication.objects.create(
            title="Postgres Administration",
            description="Intended for developers. Manage the postgres database provided by home portal and any other database that might be running.",  # noqa
            link_name="PgAdmin",
            link="/pgadmin/",
            side_menu_visible=True,
            category=category,
            side_menu_name="PgAdmin",
            side_menu_icon="DatabaseOutlined",
        )
        app.save()

        app = HomePortalApplication.objects.create(
            title="Home Portal Administration",
            description="Intended for developers and home portal administrators. Manage home portal users and configuration through the built in admin interface.",  # noqa
            link_name="Admin",
            link="/admin/",
            side_menu_visible=True,
            nav_link_visible=True,
            nav_link_name="Admin",
            nav_link_icon="TeamOutlined",
            category=category,
            side_menu_name="Admin",
            side_menu_icon="TeamOutlined",
        )
        app.save()

        app = HomePortalApplication.objects.create(
            title="Accounts",
            description="Manage your account on home portal.",
            link_name="My Account",
            link="/accounts/",
            side_menu_visible=True,
            nav_link_visible=True,
            nav_link_name="Account",
            nav_link_icon="UserOutlined",
            side_menu_name="Me",
            side_menu_icon="UserOutlined",
        )
        app.save()

        app = HomePortalApplication.objects.create(
            title="Documentation",
            description="Home portal documentation.",
            link_name="Documentation",
            link="/docs/",
            side_menu_visible=True,
            nav_link_visible=True,
            nav_link_name="Documentation",
            nav_link_icon="BookOutlined",
            side_menu_name="Documentation",
            side_menu_icon="BookOutlined",
        )
        app.save()
