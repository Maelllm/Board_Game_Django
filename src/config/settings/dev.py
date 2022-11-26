import os

from config.settings.base import *  # NOQA:

DEBUG = True

ALLOWED_HOSTS = ["*"]

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
        # "default": {
        #     "ENGINE": "django.db.backends.postgresql",
        #     "NAME": os.environ.get("POSTGRES_DB"),
        #     "USER": os.environ.get("POSTGRES_USER"),
        #     "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        #     "HOST": os.environ.get("POSTGRES_HOST"),
        #     "PORT": os.environ.get("POSTGRES_PORT"),
        # },
        # "default": {
        #     "ENGINE": "django.db.backends.postgresql",
        #     "NAME": "lyamets",
        #     "USER": "postgres",
        #     "PASSWORD": "postgres",
        #     "HOST": "localhost",
        #     "PORT": "5433",
        # }
    }

STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
