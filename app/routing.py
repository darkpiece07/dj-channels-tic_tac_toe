from django.urls import path
from . import consumers


ws_urlpatterns = [
    path('ws/game/<room_code>', consumers.GameRoom.as_asgi()),
]