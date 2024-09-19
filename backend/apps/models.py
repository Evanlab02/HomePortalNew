"""Contains models for the application managementlication."""

from django.db.models import CASCADE, BooleanField, CharField, ForeignKey, Model


class HomePortalCategory(Model):
    """Side menu category for home portal applications."""

    title = CharField(max_length=30)
    icon = CharField(max_length=30)

    def __str__(self) -> str:
        """Convert object to string representation."""
        return self.title


class HomePortalApplication(Model):
    """Application entry for the home portal application."""

    title = CharField(max_length=30)
    description = CharField(max_length=255)
    link_name = CharField(max_length=30)
    link = CharField(max_length=255)
    side_menu_visible = BooleanField(default=False)
    nav_link_visible = BooleanField(default=False)
    category = ForeignKey(HomePortalCategory, on_delete=CASCADE, default=None, null=True)
    side_menu_name = CharField(max_length=30, default="")
    side_menu_icon = CharField(max_length=30, default="")
    nav_link_name = CharField(max_length=30, default="")
    nav_link_icon = CharField(max_length=30, default="")

    def __str__(self) -> str:
        """Convert object to string representation."""
        return self.title
