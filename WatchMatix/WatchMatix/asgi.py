"""
ASGI config for WatchMatix project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing  import ProtocolTypeRputer, URLRouter 
from channels.auth import AutMiddlewareStack
import camera.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WatchMatix.settings')

application = get_asgi_application({
    "http": get_asgi_application(),
    "websocket": AutMiddlewareStack(
        URLRouter(
            camera.routing.websocker_urlpatterns
        )
    ),
})
