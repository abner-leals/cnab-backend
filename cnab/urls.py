from django.urls import path
from .views import CreateTransaction, ListBalance
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("cnab/", CreateTransaction.as_view()),
    path("balance/", ListBalance.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        (SpectacularSwaggerView.as_view(url_name="schema")),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        (SpectacularRedocView.as_view(url_name="schema")),
        name="redoc",
    ),
]
