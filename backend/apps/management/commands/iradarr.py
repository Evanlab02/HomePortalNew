"""Creates the radarr app for the home portal."""

from typing import Any, no_type_check

from django.core.management.base import BaseCommand

from apps.models import HomePortalApplication, HomePortalCategory


class Command(BaseCommand):
    """Create the radarr app for the home portal."""

    @no_type_check
    def handle(self, *args: Any, **options: Any) -> None:
        """Create the radarr app for the home portal."""
        category = HomePortalCategory.objects.get(title="Media")

        link = input(
            "Please enter your radarr link (This will be a direct link and not proxied via the HomePortal): "  # noqa
        )

        app = HomePortalApplication.objects.create(
            title="Radarr",
            description="",
            link_name="Radarr",
            link=link,
            side_menu_visible=True,
            category=category,
            side_menu_name="Radarr",
            side_menu_icon="VerticalAlignBottomOutlined",
        )
        app.save()
