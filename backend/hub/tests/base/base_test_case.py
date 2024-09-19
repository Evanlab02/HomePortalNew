"""Contains the base test case for request factory testing."""

from django.contrib.auth.models import AnonymousUser, User
from django.test import Client, TestCase

from apps.models import HomePortalApplication, HomePortalCategory


class BaseTestCase(TestCase):
    """Base test case for testing."""

    def setUp(self) -> None:
        """Set up the tests."""
        self.user = User.objects.create(
            username="testuser",
            email="testuser@gmail.com",
            password="testpass",
            first_name="Test",
            last_name="User",
        )
        self.user.save()

        self.category = HomePortalCategory.objects.create(title="Administration", icon="CodeFilled")
        self.category.save()

        self.app = HomePortalApplication.objects.create(
            title="Postgres Administration",
            description="Intended for developers. Manage the postgres database provided by home portal and any other database that might be running.",  # noqa
            link_name="PgAdmin",
            link="/pgadmin/",
        )
        self.app.save()

        self.categorized_menu_app = HomePortalApplication.objects.create(
            title="Home Portal Administration",
            description="Intended for developers and home portal administrators. Manage home portal users and configuration through the built in admin interface.",  # noqa
            link_name="Admin",
            link="/admin/",
            nav_link_visible=True,
            side_menu_visible=True,
            nav_link_name="Admin",
            nav_link_icon="TeamOutlined",
            category=self.category,
            side_menu_name="Admin",
            side_menu_icon="TeamOutlined",
        )
        self.categorized_menu_app.save()

        self.no_category_app = HomePortalApplication.objects.create(
            title="Accounts",
            description="Manage your account on home portal.",
            link_name="My Account",
            link="/accounts/",
            side_menu_name="Me",
            side_menu_icon="UserOutlined",
            nav_link_visible=False,
            side_menu_visible=True,
        )
        self.no_category_app.save()

        self.client = Client()
        self.client.force_login(self.user)

        self.titles = [self.app.title, self.categorized_menu_app.title, self.no_category_app.title]

        self.descriptions = [
            self.app.description,
            self.categorized_menu_app.description,
            self.no_category_app.description,
        ]

        self.link_names = [
            self.app.link_name,
            self.categorized_menu_app.link_name,
            self.no_category_app.link_name,
        ]

        self.links = [
            self.app.link,
            self.categorized_menu_app.link,
            self.no_category_app.link,
        ]

        return super().setUp()

    def tearDown(self) -> None:
        """Tear down the tests."""
        User.objects.all().delete()
        HomePortalApplication.objects.all().delete()
        HomePortalCategory.objects.all().delete()
        self.titles = []
        self.descriptions = []
        self.link_names = []
        self.links = []
        return super().tearDown()

    def get_anonymous_user(self) -> AnonymousUser:
        """Get an anonymous user."""
        return AnonymousUser()

    def get_user(self) -> User:
        """Get a logged in user."""
        return self.user
