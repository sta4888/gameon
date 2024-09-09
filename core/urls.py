from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from core import settings

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('userauth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Добавляем пути к статическим и медиа-файлам
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
