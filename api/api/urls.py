from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import OperacaoViewSet, UploadViewSet
from rest_framework import routers
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'operacoes', OperacaoViewSet)
router.register(r'upload', UploadViewSet)


urlpatterns = [
 	path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if not settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        
    )
    
    
if not settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

