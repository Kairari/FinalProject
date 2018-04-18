from django.contrib import admin
from .models import User
from .models import Map
from .models import Character


# Register your models here.
admin.site.register(User)
admin.site.register(Map)
admin.site.register(Character)
