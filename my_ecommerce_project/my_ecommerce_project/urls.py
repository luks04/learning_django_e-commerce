"""my_ecommerce_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_api.views import MovieViewSet

router = routers.DefaultRouter() # Imported from rest_framework
router.register('movie', MovieViewSet) # To include the viewset on the routesr.urls
'''
router.register('<ClassName with lower_case>', <ClassName>ViewSet)
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("resume.urls")),
    path('api/', include(router.urls)), # api/<registered_app_name>
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
