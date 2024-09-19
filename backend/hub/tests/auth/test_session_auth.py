"""Contains tests for the session auth ninja class."""

from django.contrib.auth.models import User

from hub.auth.session_auth import SessionAuth
from hub.tests.base.base_request_factory import BaseRequestFactoryTestCase


class TestSessionAuth(BaseRequestFactoryTestCase):
    """Contains tests for the session auth."""

    def setUp(self) -> None:
        """Set up the tests."""
        self.AUTH = SessionAuth()
        return super().setUp()

    async def test_session_auth_returns_none_with_anonymous_user(self) -> None:
        """Test that a user will be rejected if they are not logged in with session auth."""
        request = self.get_anonymous_request("")
        result = await self.AUTH.authenticate(request=request, key=None)
        self.assertIsNone(result)

    async def test_session_auth_returns_user(self) -> None:
        """Test that a user is accepted if logged in with session auth."""
        request = self.get_user_request("")
        result = await self.AUTH.authenticate(request=request, key=None)
        self.assertIsInstance(result, User)
