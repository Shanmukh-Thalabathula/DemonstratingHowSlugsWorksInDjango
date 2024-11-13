from django.urls import path
from .views import home, details, details_without_slug

urlpatterns = [
    path("", home, name="home"),
    path("details/<slug:slug>/", details, name="details"),
    path("details-without-slug/<int:id>/", details_without_slug, name="details-without-slug"),
]
