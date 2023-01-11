from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
# from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

# from django.conf.urls.static import static
from mpmu import settings
from project.urls import router as project_router


schema = get_swagger_view(title="APIs")

urlpatterns = [
    path("site-admin/", admin.site.urls),
    path('api/v1/project/', include((project_router.urls, 'project'))),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r"^__debug__/", include(debug_toolbar.urls)),
        # swagger Schema routes, Display all APIs
        path("v1/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    ]
