"""Contains the application management config."""

from logging import getLogger

from django.apps import AppConfig

log = getLogger(__name__)
log.info("application management config loading...")


class AppsConfig(AppConfig):
    """application management config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps"


log.info("application management config loaded.")
