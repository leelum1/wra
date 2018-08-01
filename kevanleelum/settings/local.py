from .base import *

MAPBOX_TOKEN = get_secret('MAPBOX_TOKEN')

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

#Debug toolbar
INTERNAL_IPS = ('127.0.0.1', 'localhost',)
MIDDLEWARE += (
   'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PANELS = [
   'debug_toolbar.panels.versions.VersionsPanel',
   'debug_toolbar.panels.timer.TimerPanel',
   'debug_toolbar.panels.settings.SettingsPanel',
   'debug_toolbar.panels.headers.HeadersPanel',
   'debug_toolbar.panels.request.RequestPanel',
   'debug_toolbar.panels.sql.SQLPanel',
   'debug_toolbar.panels.staticfiles.StaticFilesPanel',
   'debug_toolbar.panels.templates.TemplatesPanel',
   'debug_toolbar.panels.cache.CachePanel',
   'debug_toolbar.panels.signals.SignalsPanel',
   'debug_toolbar.panels.logging.LoggingPanel',
   'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
   'INTERCEPT_REDIRECTS': False,
}

DATABASES = {
    'default':{
        'NAME': get_secret('DB_NAME'),
        'ENGINE': 'django.db.backends.postgresql',
        'USER': get_secret('DB_USER'),
        'PASSWORD': get_secret('DB_PASSWORD'),
        'HOST':get_secret('DB_HOST'),
        'PORT': get_secret('DB_PORT'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = BASE_DIR / 'static_root'
STATICFILES_DIRS = [BASE_DIR / 'static']
