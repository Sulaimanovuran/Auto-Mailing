from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view as default_get_schema_view
from rest_framework.permissions import IsAuthenticated, BasePermission

from mailing_list.views import *

router = DefaultRouter()

router.register(r'mailings', MailingViewSet, basename='mailing')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'operators', OperatorViewSet, basename='operator')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
    path('get_statistics_for_all_mailings/', get_statistics_for_all_mailings,
         name='get_statistics_for_all_mailings'),
    path('get_statistics_for_mailing/<int:pk>/', get_statistics_for_mailing, name='get_statistics_for_mailing')
]


class _CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = [
            "http",
        ]
        return schema


def get_schema_view(title: str, version: str):
    return default_get_schema_view(
        openapi.Info(title=title, default_version=version),
        public=True,
        generator_class=_CustomSchemaGenerator,
        permission_classes=[IsAuthenticated, ]
    )
