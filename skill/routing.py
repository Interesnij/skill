from django.conf.urls import url

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from notifications.consumers import NotificationsConsumer
from chat.consumers import MessagerConsumer


application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                url('ws://навык.рус:8001/notifications/', NotificationsConsumer),
                url('ws://навык.рус:8001/(?P<username>[^/]+)/$', MessagerConsumer),
            ])
        ),
    ),
})
