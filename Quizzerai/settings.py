# settings.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ufd+-p5$s9rq)-7moj+_o5@1!h!p_@^2+s9)1goofy_ez)5+&8'
DEBUG = True
ALLOWED_HOSTS = []

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ALLOWED_HOSTS = ['*']


# ALLOWED_HOSTS = ['192.168.1.6', '127.0.0.1', 'localhost']


# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quizzerapp',
    'rest_framework',
    'django_extensions',
    'corsheaders',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  
]

ROOT_URLCONF = 'Quizzerai.urls'

# Template Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Quizzerai.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Quizzerai',
        'USER': 'Praveen',
        'PASSWORD': 'Praveen@28',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_Quizzerai',  
        },
    }
}

# REST Framework and Keycloak integration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'quizzerapp.authentication.KeycloakAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated', # Default to authenticated
    ]
}

# Keycloak configuration
KEYCLOAK_SERVER_URL = 'http://192.168.1.87:8080'
KEYCLOAK_REALM = 'Quizzer.ai'
KEYCLOAK_CLIENT_ID = 'Quizzer'
KEYCLOAK_CLIENT_SECRET_KEY = 'oKiZ3JmJ6xjIbLNk75Ortxt4K82C294Y'
KEYCLOAK_RETURN_URI = 'http://localhost:8000/'



APPEND_SLASH = False

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


