"""robmuze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import *

from django.conf.urls.i18n import i18n_patterns
from collabs.views import unchecked, check

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('sample/', include('samples.urls')),
    path('', include('core.urls')),
    path('ankiety/', include('ankiety.urls')),
    path('collabs/', include('collabs.urls')),
    
    path('check/', unchecked, name = "unchecked"),
    path('check/<pk>', check, name= "check-sub"),
    
    path("ideas/", include('ideas.urls')),
    
    
    
    path("__reload__/", include("django_browser_reload.urls")),
    
]

# urlpatterns += i18n_patterns(
#     path('sample/', include('samples.urls')),
#     path('', include('core.urls')),
#     path('ankiety/', include('ankiety.urls')),
#     path('collabs/', include('collabs.urls')),
#     prefix_default_language=False
# )

if settings.DEBUG:
    # dont do this in prod
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)