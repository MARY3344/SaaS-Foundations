"""
WSGI config for cfehome project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# import os#error fix
# import django#error fix
# from django.core.management import call_command ##error fix
from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings') #error fix

# django.setup()#error fix
# call_command('migrate')#error fix

application = get_wsgi_application()

