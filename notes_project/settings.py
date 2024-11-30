from pathlib import Path
import pymongo

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-88fc9!52=yh$@9czc=xetfi1pa6==mip0-b6oh^-)*_+iak60m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1', 
    'notes-project-yywg.onrender.com'  # Your live server's URL
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',  # Add this for CORS support
    'notes',  # Your notes app
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Add this middleware for CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'notes_project.urls'

# CORS configuration
CORS_ALLOW_ALL_ORIGINS = True  # For development. Change to `False` for production and specify origins

# Optionally, specify specific origins for production:
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000',  # Frontend URL for development
#     'https://yourfrontenddomain.com',  # Your production frontend URL
# ]

# Allow specific methods for CORS
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]

# Allow specific headers for CORS
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',  # Useful if you're dealing with CSRF protection
]

# Allow cookies to be sent with cross-origin requests (useful if using sessions or authentication)
CORS_ALLOW_CREDENTIALS = True


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

WSGI_APPLICATION = 'notes_project.wsgi.application'


# Database
# SQLite Database (local development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# MongoDB Configuration
MONGO_CLIENT = pymongo.MongoClient('mongodb+srv://125003302:sethu@assault-seathu.s3amc.mongodb.net/?retryWrites=true&w=majority&appName=assault-seathu')
MONGO_DATABASE = MONGO_CLIENT['assault-seathu']


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
