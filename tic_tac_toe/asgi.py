import os
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application
import app.routing
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dc1.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            app.routing.ws_urlpatterns
        )
    )
})

