"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from api.resources import UserResource
from api.resources import MapResource
from api.resources import CharacterResource

user_resource = UserResource()
map_resource = MapResource()
character_resource = CharacterResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(user_resource.urls)),
    path('api/', include(map_resource.urls)),
    path('api/', include(character_resource.urls)),
]
