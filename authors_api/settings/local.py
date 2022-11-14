from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
        "DJANGO_SECRET_KEY",
        default="Pcote238jhejebihbe2822ebibrb3yfbdjs$djjdkwk919811919eee7e77ekbsdkudnhcb6628dsbvhv",
    )
# SECRET_KEY = 'django-insecure-a-mclstxumb_&xh7c!^9jcrn3-@&7e81b02w10-1qr3g3zay%('


ALLOWED_HOSTS = ["localhost","0.0.0.0","127.0.0.1"]