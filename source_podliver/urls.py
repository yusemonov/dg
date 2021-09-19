import debug_toolbar
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path

urlpatterns = [
    path('', include('idgenerator.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),

]
