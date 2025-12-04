import os
from pathlib import Path
import dj_database_url

# --------------------------------------------------
# BASE SETTINGS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET KEY
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "dev-secret-key"  # fallback for local development
)

# DEBUG
DEBUG = os.environ.get("DEBUG", "False") == "True"

# ALLOWED HOSTS
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# Fix CSRF when deploying to Render
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]

# --------------------------------------------------
# INSTALLED APPS
# --------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "graphene_django",
]

GRAPHENE = {
    "SCHEMA": "bankapi.schema.schema"
}

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # <--- added

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --------------------------------------------------
# URLS / WSGI
# --------------------------------------------------

ROOT_URLCONF = "bankapi.urls"

WSGI_APPLICATION = "bankapi.wsgi.application"

# --------------------------------------------------
# DATABASE SETTINGS
# --------------------------------------------------

# Default local DB (for development)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bankdb",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Override database if DATABASE_URL present (Render / production)
DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    DATABASES["default"] = dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        ssl_require=False,
    )

# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --------------------------------------------------
# DEFAULT AUTO FIELD
# --------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
