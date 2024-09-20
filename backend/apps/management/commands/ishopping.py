"""Initializes the application with all its groups and permissions."""

from typing import Any, no_type_check

from django.core.management.base import BaseCommand

from apps.models import HomePortalApplication, HomePortalCategory


class Command(BaseCommand):
    """Create shopping application and category."""

    @no_type_check
    def handle(self, *args: Any, **options: Any) -> None:
        """Create shopping application and category."""
        category = HomePortalCategory.objects.create(title="Shopping", icon="ShoppingCartOutlined")
        category.save()

        app = HomePortalApplication.objects.create(
            title="Shopping List App",
            description="Shopping app that allows users to manage their shopping lists within their household via the home portal.",  # noqa
            link_name="Shopping List App",
            link="http://localhost:9999/shopping/dashboard/",
            side_menu_visible=True,
            category=category,
            side_menu_name="Shopping List App",
            side_menu_icon="ShoppingCartOutlined",
        )
        app.save()

        app = HomePortalApplication.objects.create(
            title="Shopping List App Admin",
            description="Admin page for the home portal shopping list app.",  # noqa
            link_name="Shopping List App Admin",
            link="http://localhost:9999/admin/",
            side_menu_visible=True,
            category=category,
            side_menu_name="Shopping List App Admin",
            side_menu_icon="TeamOutlined",
        )
        app.save()
