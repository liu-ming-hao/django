"""
Django settings for meetingroom project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path






# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


LOG_DIR = BASE_DIR / "logs"
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uv7*q+7-vf^wtr(mdt@&6jz3)sucjt=_nya06^*%=tl1*&ra=o'

# 文件上传配置
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DINGTALK_WEB_HOOK = 'https://oapi.dingtalk.com/robot/send?access_token=2e55053d802ae0cc023b2c3080d3ee0463127c60d893fcec87a3f44cf40cfca0'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': { # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(lineno)d %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },

        'mail_admins': { # Add Handler for mail_admins for `warning` and above
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file': {
            #'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, 'recruitment.admin.log'),
        },

        'performance': {
            #'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, 'recruitment.performance.log'),
        },
    },

    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },

    'loggers': {
        "django_python3_ldap": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
        },

        "interview.performance": {
            "handlers": ["console", "performance"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

# Application definition

LOGIN_REDIRECT_URL = '/' #登录成功跳转地址

SIMPLE_BACKEND_REDIRECT_URL = '/accounts/login/' #匿名用户登录跳转地址

INSTALLED_APPS = [
    'bootstrap4', #主题
    'grappelli', #主题
    'registration', #匿名用户注册
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', #restful接口
    'jobs', #招聘信息
    'interview', #面试信息
]

MIDDLEWARE = [
    'interview.performance.PerformanceAndExceptionLoggerMiddleware',#引入自定义日志中间件
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', #多语言支持中间件
    'django.middleware.cache.UpdateCacheMiddleware', #缓存中间件
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware', #缓存中间件
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meetingroom.urls'

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

WSGI_APPLICATION = 'meetingroom.wsgi.application'

# restful接口配置
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

#LANGUAGE_CODE = 'zh-hans'
#LANGUAGE_CODE = 'en-us'
#修改为中国时间TIME_ZONE
#TIME_ZONE = 'Asia/Shanghai'
#TIME_ZONE = 'UTC'
from django.utils.translation import gettext_lazy as _ # 多语言支持包

LANGUAGES = [
    ('zh-hans', _('Chinese')),
    ('en', _('English')),
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
