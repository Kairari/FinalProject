from django.db import models

class User(models.Model):
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def set_password(self, newpassword):
        self.password = newpassword
        self.save()

    def __str__(self):
        return self.email

class Map(models.Model):
    name = models.CharField(max_length=200)
    map_columns = models.IntegerField()
    map_rows = models.IntegerField()
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=200)
    max_health = models.IntegerField()
    current_health = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_map = models.ManyToManyField(Map, blank=True)
    character_position = models.IntegerField(blank=True)

    def set_max_health(self, number):
        self.max_health = number
        self.save()

    def set_current_health(self, number):
        self.current_health = number
        self.save()

    def set_character_position(self, number):
        character_position = number
        self.save()

    def __str__(self):
        return self.name
# Create your models here.
