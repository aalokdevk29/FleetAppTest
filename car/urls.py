from django.urls import path

from car.api import views


urlpatterns = [
    # Car API Endpoints
    path(
        "cars:list/",
        views.CarList.as_view(),
        name="car-list"
    ),
    path(
        "cars:create/",
        views.CarCreate.as_view(),
        name="car-create"
    ),
    path(
        "cars:retrieve/",
        views.CarDetail.as_view(),
        name="car-detail"
    ),
    path(
        "cars:update/",
        views.CarUpdate.as_view(),
        name="car-update"
    ),
    path(
        "cars:delete/",
        views.CarDelete.as_view(),
        name="car-delete"
    ),
]
