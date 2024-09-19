"""Contains the base test case for request factory testing."""

from asgiref.sync import sync_to_async
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpRequest
from django.test import AsyncRequestFactory, TestCase


class BaseRequestFactoryTestCase(TestCase):
    """Base test case for request factory testing."""

    def setUp(self) -> None:
        """Set up the tests."""
        self.factory = AsyncRequestFactory()
        self.user = User.objects.create(
            username="testuser",
            email="testuser@gmail.com",
            password="testpass",
            first_name="Test",
            last_name="User",
        )
        self.user.save()
        return super().setUp()

    def tearDown(self) -> None:
        """Tear down the tests."""
        User.objects.all().delete()
        return super().tearDown()

    def get_anonymous_request(self, path: str) -> HttpRequest:
        """Get a request with an anonymous user."""
        request = self.factory.get(path)
        mock_user_func = lambda: AnonymousUser()  # noqa
        async_mock_user_func = sync_to_async(mock_user_func)
        request.auser = async_mock_user_func
        return request

    def get_user_request(self, path: str) -> HttpRequest:
        """Get a request with a valid user."""
        request = self.factory.get(path)
        mock_user_func = lambda: self.user  # noqa
        async_mock_user_func = sync_to_async(mock_user_func)
        request.auser = async_mock_user_func
        return request
