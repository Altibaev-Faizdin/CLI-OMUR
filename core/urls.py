from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from core.yasg import urlpatterns_yasg

landing_urls = [
    path("admin/", admin.site.urls),
    path("v1/", include("apps.settings.urls")),
    path("", include(urlpatterns_yasg)),
    re_path(r'^back_media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),

]
urlpatterns = [
    path("api/landing/", include(landing_urls))
]
