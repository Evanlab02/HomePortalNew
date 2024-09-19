"""Contains tests for the user repository."""

from hub.database.user_repo import UserRepo
from hub.tests.base.base_test_case import BaseTestCase


class TestUserRepo(BaseTestCase):
    """Test the user repo."""

    def setUp(self) -> None:
        """Set up the tests."""
        self.repo = UserRepo()
        return super().setUp()

    async def test_is_user_authenticated_with_anonymous_user(self) -> None:
        """Test the is authenticated function with an anonymous user."""
        user = self.get_anonymous_user()
        result = self.repo.is_user_authenticated(user=user)
        self.assertFalse(result)

    async def test_is_user_authenticated(self) -> None:
        """Test the is authenticated function with a logged in user."""
        user = self.get_user()
        result = self.repo.is_user_authenticated(user=user)
        self.assertTrue(result)
