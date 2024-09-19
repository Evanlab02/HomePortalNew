"""Contains tests for the models of the application management app."""

from apps.models import HomePortalApplication, HomePortalCategory
from hub.tests.base.base_test_case import BaseTestCase


class TestAppsModels(BaseTestCase):
    """Contains tests for the models."""

    def test_category_to_string(self) -> None:
        """Test that a category model returns the correct string representation."""
        result = str(self.category)
        self.assertIsInstance(self.category, HomePortalCategory)
        self.assertEqual(result, self.category.title)

    def test_application_to_string(self) -> None:
        """Test that a application model returns the correct string representation."""
        result = str(self.app)
        self.assertIsInstance(self.app, HomePortalApplication)
        self.assertEqual(result, self.app.title)
