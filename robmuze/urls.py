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

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path('inbox/', include('conversation.urls')),
    path('sample/', include('samples.urls')),
    path('', include('core.urls')),
    # path('dash/', include('userdash.urls'), name='dash')
    path('ankiety/', include('ankiety.urls')),
    path('collabs/', include('collabs.urls')),
]


if settings.DEBUG:
    # dont do this in prod
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)