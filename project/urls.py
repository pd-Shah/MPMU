from rest_framework.routers import DefaultRouter

from .apis import (
    ViewSetProject,
    ViewSetTimeLine,
)

router = DefaultRouter()
router.register(r'', ViewSetProject, basename='project')
router.register(r'timeline', ViewSetTimeLine, basename='timeline')
urlpatterns = router.urls
