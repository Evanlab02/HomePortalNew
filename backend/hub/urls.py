"""
URL configuration for hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import logging

from django.http import HttpRequest, HttpResponsePermanentRedirect
from django.urls import include, path
from ninja import NinjaAPI

from apps.routers.app_router import app_router

api = NinjaAPI(title="Home Portal API")
api.add_router("/applications", app_router)

log = logging.getLogger(__name__)
log.info("HUB URLs loading...")


def redirect_fix(request: HttpRequest) -> HttpResponsePermanentRedirect:
    """Temporary redirect fix for allauth."""
    return HttpResponsePermanentRedirect("/accounts/email/")


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("accounts/profile/", redirect_fix),
    path("api/v1/", api.urls),
]

log.info("HUB URLs loaded.")
