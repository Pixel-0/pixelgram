from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from gram import urls

urlpatterns = [
    url('', include('gram.urls')),
    url('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
