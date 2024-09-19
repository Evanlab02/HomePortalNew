"""
ASGI config for hub project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import logging
import os

from django.core.asgi import get_asgi_application

log = logging.getLogger(__name__)
log.info("ADMIN HUB ASGI config loading...")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hub.admin.admin_settings")

application = get_asgi_application()
log.info("ADMIN HUB ASGI config loaded.")
