"""Contains checks to ensure HUB local settings are correct."""

from hub.dev.local_settings import (
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
    """Test the secret key is correctly set from the local settings."""
    assert SECRET_KEY == "LOCAL_SECRET_KEY"


def test_debug_value() -> None:
    """Test the debug value is correctly set from the local settings."""
    assert DEBUG is True


def test_allowed_hosts_value() -> None:
    """Test the allowed hosts value is correctly set from the local settings."""
    assert len(ALLOWED_HOSTS) == 1
    assert ALLOWED_HOSTS[0] == "*"


def test_root_url_conf_value() -> None:
    """Test the root url configuration value is correctly set from the local settings."""
    assert ROOT_URLCONF == "hub.dev.urls"


def test_databases_config() -> None:
    """Test the databases configuration is correctly set from the local settings."""
    DEFAULT_DB = DATABASES.get("default")
    assert DEFAULT_DB is not None

    ENGINE = DEFAULT_DB.get("ENGINE")

    assert ENGINE == "django.db.backends.sqlite3"


def test_static_root_and_url() -> None:
    """Test the static configuration is correctly set from the local settings."""
    assert STATIC_URL == "static/"
    assert STATIC_ROOT == "static/"


def test_password_hashers() -> None:
    """Test the password hasher config is correctly set from the local settings."""
    assert len(PASSWORD_HASHERS) == 1
    assert PASSWORD_HASHERS[0] == "django.contrib.auth.hashers.Argon2PasswordHasher"


def test_account_email_verification() -> None:
    """Test the account email verfication config is correctly set from the local settings."""
    assert ACCOUNT_EMAIL_VERIFICATION == "none"
