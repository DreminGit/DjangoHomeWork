"""
WSGI конфигурация для настройки проекта.

Он предоставляет возможность вызова WSGI в качестве переменной уровня модуля с именем `application`.

Для получения дополнительной информации об этом файле:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()