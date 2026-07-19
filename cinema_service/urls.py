from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("api/cinema/genres/", include("cinema.urls", namespace="genres")),
    path("api/cinema/actors/", include("cinema.urls", namespace="actors")),
    path("api/cinema/actors/cinema_halls/", include("cinema.urls", namespace="cinema_halls")),
]
