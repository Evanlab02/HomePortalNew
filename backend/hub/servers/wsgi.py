"""
WSGI config for hub project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import logging
import os

from django.core.wsgi import get_wsgi_application

log = logging.getLogger(__name__)
log.info("HUB WSGI config loading...")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hub.settings.settings")

application = get_wsgi_application()
log.info("HUB WSGI config loaded.")
