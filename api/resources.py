from tastypie.resources import ModelResource
from .models import User
from .models import Map
from .models import Character
from tastypie.authorization import Authorization

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()

class MapResource(ModelResource):
    class Meta:
        queryset = Map.objects.all()
        resource_name = 'map'
        authorization = Authorization()

class CharacterResource(ModelResource):
    class Meta:
        queryset = Character.objects.all()
        resource_name = 'map'
        authorization = Authorization()
