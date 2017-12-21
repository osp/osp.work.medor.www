# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Django settings for medor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
gettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_ID = 1

# Application definition

ROOT_URLCONF = 'medor.urls'

WSGI_APPLICATION = 'medor.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr'
LANGUAGES = [('fr', 'Francais'),]
DEFAULT_LANGUAGE = 0

TIME_ZONE = 'Europe/Brussels'

USE_I18N = True

USE_L10N = True

USE_TZ = True





# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'compressor',

    'subscribe',
    'collaborate',

    'cms',  # django CMS itself
    'treebeard',
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for javascript and css management
    'reversion',
    'filer',
    'easy_thumbnails',
    'djangocms_text_ckeditor',  # note this needs to be above the 'cms' entry

    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    ## Django CMS Blog
    #'filer',
    #'easy_thumbnails',
    #'cmsplugin_filer_image',
    # 'parler',
    # 'taggit',
    # 'taggit_autosuggest',
    # 'django_select2',
    # 'meta',
    # 'meta_mixin',
    # 'admin_enhancer',
    # 'djangocms_blog',

    'registration',

    'django.contrib.sitemaps',

    'publish',
    'adminsortable2',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'corsheaders',
    'ckeditor',

    'reversion_compare', # https://github.com/jedie/django-reversion-compare

    'formtools',

    'buy'
)

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]


TEMPLATES = [
    {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'DIRS': (os.path.join(BASE_DIR, "medor", "templates"),),
    'OPTIONS': {
        'context_processors':
        (
        'django.contrib.auth.context_processors.auth',
        'django.template.context_processors.debug',
        'django.template.context_processors.i18n',
        'django.template.context_processors.media',
        'django.template.context_processors.static',
        'django.template.context_processors.tz',
        'django.template.context_processors.csrf',
        'django.template.context_processors.request',
        'django.contrib.messages.context_processors.messages',
        'sekizai.context_processors.sekizai',
        'cms.context_processors.cms_settings',
        ),
    }
    },
]

# TEMPLATE_DIRS = (
    # # The docs say it should be absolute path: BASE_DIR is precisely one.
    # # Life is wonderful!
    # os.path.join(BASE_DIR, "medor", "templates"),
# )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = "/media/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "medor", "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Django Compressor setup
COMPRESS_PRECOMPILERS = (
   ('text/less', 'lessc {infile} > {outfile}'),
)
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]

# This is so the {% if debug %} works,
# cf http://stackoverflow.com/questions/11020663/
INTERNAL_IPS = ('127.0.0.1',)

CMS_TEMPLATES = (
    ('page.html', 'Page (simple)'),
    ('styleguide.html', 'Feuille de style'),
    ('where-to-buy.html', 'Obtenir Médor'),
    ('magazine.html', 'Le magazine')
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar': 'CMS',
    'skin': 'moono',
    'stylesSet': 'medor:/static/djangocms_text_ckeditor/ckeditor/styles.js'
}

TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

META_USE_SITES = True

PARLER_LANGUAGES = {
    1: (
        {'code': 'fr',},
    ),
}


ACCOUNT_ACTIVATION_DAYS = 1 # One-day activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.
REGISTRATION_OPEN = False
DEFAULT_FROM_EMAIL = "medor@medor.coop"

# make passwords stronger
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #  'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}


CORS_ORIGIN_REGEX_WHITELIST = ('^(https?://)?(\w+\.)?localhost(:\d+)?$', )
CORS_ALLOW_CREDENTIALS = True


CKEDITOR_JQUERY_URL = '/static/components/jquery/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'format_tags': 'chapeau;intertitre;surtitre;question;normal',
        'format_chapeau': {'element': 'p', 'name' : 'Chapô', 'attributes' : {'class' : 'chapeau'}},
        'format_intertitre': {'element': 'h2', 'name' : 'Intertitre'},
        'format_surtitre': {'element': 'h3', 'name' : 'Sur- ou sous-titre'},
        'format_question': {'element': 'p', 'name' : 'Question', 'attributes' : {'class' : 'question'}},
        'format_normal': {'element': 'p', 'name' : 'Texte normal'},
        'entities': False,
        'image2_captionedClass': '',
        'wordcount': {
            'showCharCount': True,
            'countSpacesAsChars': True
        },
        'extraAllowedContent': '; '.join([
            'h1 abbr figure figcaption footer small dl dt dd',
            'div[class]',
            'aside[id](exergue,making-of,encadre,pull-out,sidebar,footnotes)',
            'p(chapeau,intro-medor,question,auteur,fin,debut,footer-byline,endnote)',
            'ol(footnotes)',
            'img[data-*]{margin,max-width,margin}',
            'video[controls,src]',
            'span(lettrine,print-only,auteur,ellipsis,blank,keep)',
            'iframe[src,width,height,frameborder,webkitallowfullscreen,mozallowfullscreen,allowfullscreen]',
        ]),
        'image2_prefillDimensions': False,
        'admin_url': '/admin/',
        'contentsCss': 'https://medor.coop/static/CACHE/css/f3b96be794f8.css',
        'toolbar_Custom': [
            ['Format'],
            ['Pull-out', 'Sidebar', 'Footer'],
            ['Bold', 'Italic', '-', 'Subscript', 'Superscript'],
            ['BulletedList', 'NumberedList', '-', 'Outdent', 'Indent', '-', ''],
            ['Link', 'Unlink', 'Image'],
            ['RemoveFormat', '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', 'SpecialChar'],
            ['Source', 'Maximize'
                # ,'Footnotes'
                #'Filer Image'
            ],
        ],
        'extraPlugins': ','.join([
            'wordcount',
            'notification',
            'image2',
            'pull-out',
            'footer',
            'sidebar',
            # 'footnotes'
            #'filerimage'
        ]),
    }
}

# Add reversion models to admin interface:
ADD_REVERSION_ADMIN=True


try:
    LOCAL_SETTINGS
except NameError:
    try:
        from local_settings import *
    except ImportError:
        pass
