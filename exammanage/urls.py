from django.contrib import admin
from django.urls import path, include
from core.views import Imtahan, DuzgunCavab

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Imtahan.as_view(), name='index'),
    path('dg/<int:pk>', DuzgunCavab.as_view(), name='exam_correct'),
    path('', include('django.contrib.auth.urls')),

]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
