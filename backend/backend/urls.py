from django.contrib import admin
from django.urls import include, path
from health_check.views import HealthCheckView
from rest_framework import routers

from api import views
from config import app_config

router = routers.DefaultRouter()
router.register("tasks", views.TaskView, "task")

urlpatterns = [
    path(app_config.django.admin_path, admin.site.urls),
    path(
        app_config.django.healthcheck_path,
        HealthCheckView.as_view(
            checks=[
                "health_check.Database",
                "health_check.Storage",
                "health_check.Cache",
            ]
        ),
        name="health_check",
    ),
    path("api/", include(router.urls)),
]
