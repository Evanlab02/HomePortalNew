"""Creates the development applications for the home portal."""

from typing import Any, no_type_check

from django.core.management.base import BaseCommand

from apps.models import HomePortalApplication, HomePortalCategory


class Command(BaseCommand):
    """Create the development applications for the home portal."""

    @no_type_check
    def handle(self, *args: Any, **options: Any) -> None:
        """Create the development applications for the home portal."""
        category = HomePortalCategory.objects.create(title="Development", icon="CodeFilled")
        category.save()

        app = HomePortalApplication.objects.create(
            title="Home Portal Storybook",
            description="Intended for developers. View the storybook for the home portal components.",  # noqa
            link_name="Storybook",
            link="/components/",
            side_menu_visible=True,
            category=category,
            side_menu_name="Home Portal Storybook",
            side_menu_icon="DesktopOutlined",
        )
        app.save()

        app = HomePortalApplication.objects.create(
            title="Coverage Report - API",
            description="Intended for developers. View the coverage report for the home portal API.",  # noqa
            link_name="Coverage Report",
            link="/dev/coverage/api/",
            side_menu_visible=True,
            category=category,
            side_menu_name="Coverage Report - API",
            side_menu_icon="CheckSquareOutlined",
        )
        app.save()
