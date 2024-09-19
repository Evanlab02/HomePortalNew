"""Contains the session authentication class."""

import logging
from typing import Any, Optional

from django.conf import settings
from django.http import HttpRequest
from ninja.security.apikey import APIKeyCookie

from hub.database.user_repo import UserRepo

log = logging.getLogger(__name__)
log.info("Loading ninja session auth...")


class SessionAuth(APIKeyCookie):
    """Reusing Django session authentication."""

    param_name: str = settings.SESSION_COOKIE_NAME

    async def authenticate(self, request: HttpRequest, key: Optional[str]) -> Optional[Any]:
        """Authenticate the user."""
        repo = UserRepo()
        user = await request.auser()
        if repo.is_user_authenticated(user):
            return user

        return None


log.info("Loaded ninja session auth.")
