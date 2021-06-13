from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import login, logout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'accounts/login/$', login, name='login'),
    url(r'accounts/logout/$',logout, name='logout', kwargs={'next_page': '/'}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
