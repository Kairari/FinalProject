from tastypie.resources import ModelResource
from .models import User
from .models import Map
from .models import Character
from tastypie.authorization import Authorization
from tastypie import fields, utils
from tastypie.constants import ALL, ALL_WITH_RELATIONS


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        include_resource_uri = False
        authorization = Authorization()
        filtering = {
            'email' : ALL,
            'password' : ALL,
            'id' : ALL,
        }

class MapResource(ModelResource):
    user = fields.ToManyField(UserResource, 'user')

    class Meta:
        queryset = Map.objects.all()
        resource_name = 'map'
        include_resource_uri = False
        authorization = Authorization()
        filtering = {
            'user' : ALL_WITH_RELATIONS,
        }

class CharacterResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)
    Map = fields.ForeignKey(MapResource, 'map', null=True)

    class Meta:
        queryset = Character.objects.all()
        resource_name = 'character'
        include_resource_uri = False
        authorization = Authorization()
        filtering = {
            'user' : ALL_WITH_RELATIONS,
        }
