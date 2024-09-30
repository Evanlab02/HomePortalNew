"""Creates the plex app for the home portal."""

from typing import Any, no_type_check

from django.core.management.base import BaseCommand

from apps.models import HomePortalApplication, HomePortalCategory


class Command(BaseCommand):
    """Create the plex app for the home portal."""

    @no_type_check
    def handle(self, *args: Any, **options: Any) -> None:
        """Create the plex app for the home portal."""
        category = HomePortalCategory.objects.get(title="Media")

        link = input(
            "Please enter your plex link (This will be a direct link and not proxied via the HomePortal): "  # noqa
        )

        app = HomePortalApplication.objects.create(
            title="Plex",
            description="Plex is a media server that allows you to stream your media to any device.",  # noqa
            link_name="Plex",
            link=link,
            side_menu_visible=True,
            category=category,
            side_menu_name="Plex",
            side_menu_icon="PlayCircleOutlined",
        )
        app.save()
