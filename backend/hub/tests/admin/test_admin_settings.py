"""Contains checks to ensure HUB admin settings are correct."""

from hub.admin.admin_settings import (
    ACCOUNT_EMAIL_VERIFICATION,
    ALLOWED_HOSTS,
    DATABASES,
    DEBUG,
    PASSWORD_HASHERS,
    ROOT_URLCONF,
    SECRET_KEY,
    STATIC_ROOT,
    STATIC_URL,
)


def test_secret_key() -> None:
    """Test the secret key is correctly set from the admin settings."""
    assert SECRET_KEY == "TESTING_HP_API_DJANGO_KEY"


def test_debug_value() -> None:
    """Test the debug value is correctly set from the admin settings."""
    assert DEBUG is False


def test_allowed_hosts_value() -> None:
    """Test the allowed hosts value is correctly set from the admin settings."""
    assert len(ALLOWED_HOSTS) == 1
    assert ALLOWED_HOSTS[0] == "TESTING_HP_API_DJANGO_HOST"


def test_root_url_conf_value() -> None:
    """Test the root url configuration value is correctly set from the admin settings."""
    assert ROOT_URLCONF == "hub.admin.urls"


def test_databases_config() -> None:
    """Test the databases configuration is correctly set from the admin settings."""
    DEFAULT_DB = DATABASES.get("default")
    assert DEFAULT_DB is not None

    ENGINE = DEFAULT_DB.get("ENGINE")
    NAME = DEFAULT_DB.get("NAME")
    USER = DEFAULT_DB.get("USER")
    PASSWORD = DEFAULT_DB.get("PASSWORD")
    HOST = DEFAULT_DB.get("HOST")
    PORT = DEFAULT_DB.get("PORT")
    CONN_MAX_AGE = DEFAULT_DB.get("CONN_MAX_AGE")

    assert ENGINE == "django.db.backends.postgresql"
    assert NAME == "home-portal-db"
    assert USER == "postgres"
    assert PASSWORD == "TESTING_HP_API_DATABASE_PASSWORD"
    assert HOST == "TESTING_HP_API_DB_HOST"
    assert PORT == "5432"
    assert CONN_MAX_AGE == 0


def test_static_root_and_url() -> None:
    """Test the static configuration is correctly set from the admin settings."""
    assert STATIC_URL == "static/"
    assert STATIC_ROOT == "static/"


def test_password_hashers() -> None:
    """Test the password hasher config is correctly set from the admin settings."""
    assert len(PASSWORD_HASHERS) == 1
    assert PASSWORD_HASHERS[0] == "django.contrib.auth.hashers.Argon2PasswordHasher"


def test_account_email_verification() -> None:
    """Test the account email verfication config is correctly set from the admin settings."""
    assert ACCOUNT_EMAIL_VERIFICATION == "none"
