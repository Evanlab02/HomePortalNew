"""Contains the admin configuration for the application management app."""

import logging

from django.contrib import admin

from apps.models import HomePortalApplication, HomePortalCategory

log = logging.getLogger(__name__)
log.info("Application management app admin loading...")

admin.site.register(HomePortalCategory)
admin.site.register(HomePortalApplication)

log.info("Application management admin loaded.")
