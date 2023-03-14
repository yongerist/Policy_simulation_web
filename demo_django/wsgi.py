"""
WSGI config for demo_django project.

It exposes the WSGI callable as a module-level variable named ``application``.
 用于接收网络请求,不需要修改  同步式
For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_django.settings')

application = get_wsgi_application()
