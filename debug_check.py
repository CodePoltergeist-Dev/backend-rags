import os, django, traceback
os.environ.setdefault('DJANGO_SETTINGS_MODULE','backend.settings')
try:
    django.setup()
    from django.apps import apps
    print('api app models:', list(apps.get_app_config('api').models.keys()))
except Exception as e:
    print('Exception during django.setup:', e)
    traceback.print_exc()
