from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),
    path('api/catalog/', include('catalog.urls')), 
    path('catalog/', include('catalog.urls')), 
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

handler400 = 'catalog.views.book.error_400'
handler403 = 'catalog.views.book.error_403'
handler404 = 'catalog.views.book.error_404'
handler500 = 'catalog.views.book.error_500'