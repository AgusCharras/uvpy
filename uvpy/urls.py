from django.contrib import admin
from django.urls import path
from web.views import home, ver_carreras
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('carreras/', ver_carreras, name='ver_carreras')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
