from django.contrib import admin
from .models import Game

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ["room_code", "game_creator", "game_opponent", "is_over"]

admin.site.register(Game, GameAdmin)
