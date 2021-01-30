from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),]


