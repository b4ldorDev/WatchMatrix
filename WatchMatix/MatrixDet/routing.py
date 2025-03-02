from django.urls import re_path
from . import consumers

websocket_urlpatterns =[
    re_path(r'ws/camera/stream/$', consumers.CameraConsumer.as_asgi()),
]

