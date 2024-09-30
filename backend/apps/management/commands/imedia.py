"""Creates the media category for the home portal."""

from typing import Any, no_type_check

from django.core.management.base import BaseCommand

from apps.models import HomePortalCategory


class Command(BaseCommand):
    """Create the media category for the home portal."""

    @no_type_check
    def handle(self, *args: Any, **options: Any) -> None:
        """Create the media category for the home portal."""
        category = HomePortalCategory.objects.create(title="Media", icon="PlayCircleOutlined")
        category.save()
