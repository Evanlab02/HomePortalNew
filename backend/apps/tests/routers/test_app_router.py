"""Tests for the application router of the application management app."""

from hub.tests.base.base_test_case import BaseTestCase


class TestAppRouter(BaseTestCase):
    """Contains tests for the app router."""

    def test_get_applications(self) -> None:
        """Test the get applications endpoint."""
        response = self.client.get("/api/v1/applications")
        status = response.status_code
        self.assertEqual(status, 200)

        response_body = response.json()
        applications = response_body["applications"]
        self.assertEqual(len(applications), 3)

        for app in applications:
            title = app["title"]
            description = app["description"]
            link_name = app["link_name"]
            link = app["link"]

            self.assertTrue(title in self.titles)
            self.assertTrue(description in self.descriptions)
            self.assertTrue(link_name in self.link_names)
            self.assertTrue(link in self.links)

            self.titles.remove(title)
            self.descriptions.remove(description)
            self.link_names.remove(link_name)
            self.links.remove(link)

        self.assertEqual(len(self.titles), 0)
        self.assertEqual(len(self.descriptions), 0)
        self.assertEqual(len(self.link_names), 0)
        self.assertEqual(len(self.links), 0)

    def test_nav_menu_items(self) -> None:
        """Test the get nav menu items endpoint."""
        response = self.client.get("/api/v1/applications/navmenu")
        status = response.status_code
        self.assertEqual(status, 200)

        response_body = response.json()
        applications = response_body["applications"]
        self.assertEqual(len(applications), 1)

        app = applications[0]
        self.assertEqual(app["link"], self.categorized_menu_app.link)
        self.assertEqual(app["nav_link_name"], self.categorized_menu_app.nav_link_name)
        self.assertEqual(app["nav_link_icon"], self.categorized_menu_app.nav_link_icon)

    def test_side_menu_items(self) -> None:
        """Test the get side menu items endpoint."""
        response = self.client.get("/api/v1/applications/sidemenu")
        status = response.status_code
        self.assertEqual(status, 200)

        response_body = response.json()
        categories = response_body["categories"]
        self.assertEqual(len(categories), 1)

        category_object = categories[0]
        category = category_object["category"]
        icon = category_object["icon"]
        self.assertEqual(category, self.category.title)
        self.assertEqual(icon, self.category.icon)

        applications_for_category = category_object["applications"]
        self.assertEqual(len(applications_for_category), 1)

        categorized_side_menu_app = applications_for_category[0]
        self.assertEqual(categorized_side_menu_app["link"], self.categorized_menu_app.link)
        self.assertEqual(
            categorized_side_menu_app["side_menu_name"], self.categorized_menu_app.side_menu_name
        )
        self.assertEqual(
            categorized_side_menu_app["side_menu_icon"], self.categorized_menu_app.side_menu_icon
        )
