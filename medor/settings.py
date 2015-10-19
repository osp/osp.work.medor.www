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
    'mptt',
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
    'parler',
    'taggit',
    'taggit_autosuggest',
    'django_select2',
    'meta',
    'meta_mixin',
    'admin_enhancer',
    'djangocms_blog',

    'django.contrib.webdesign',

    'registration',

    'django.contrib.sitemaps',

    'publish',
    'adminsortable2',
    'rest_framework',
    'corsheaders',
    'ckeditor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)

TEMPLATE_DIRS = (
    # The docs say it should be absolute path: BASE_DIR is precisely one.
    # Life is wonderful!
    os.path.join(BASE_DIR, "medor", "templates"),
)

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
    ('generic.html', 'Generic'),
    ('subscribe/home.html', 'Appel'),
    ('subscribe/home2.html', 'Appel2'),
    ('subscribe/FAQ.html', 'FAQ'),
    ('styleguide.html', 'Feuille de style')
)

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'menus': 'menus.migrations_django',
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
    'filer': 'filer.migrations_django',
    'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
}

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
DEFAULT_FROM_EMAIL = "medor@medor.coop"


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


CORS_ORIGIN_REGEX_WHITELIST = ('^(https?://)?(\w+\.)?localhost(:\d+)?$', )
CORS_ALLOW_CREDENTIALS = True


CKEDITOR_JQUERY_URL = '/static/components/jquery/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'format_tags': 'p;h2;h3',
        'entities': False,
        'image2_captionedClass': '',
        'extraAllowedContent': 'h1 abbr figure figcaption dl dt dd; aside(exergue); div p(chapeau,intro-medor,question); ol(footnotes)',
        'image2_prefillDimensions': False,
        'admin_url': '/admin/',
        'toolbar_Custom': [
            ['Format'],
            ['Bold', 'Italic', '-', 'Subscript', 'Superscript'],
            ['BulletedList', 'NumberedList', '-', 'Outdent', 'Indent', '-', 'Blockquote'],
            ['Link', 'Unlink', 'Image'],
            ['RemoveFormat', '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Find', 'Replace'],
            ['Source', 'Maximize'
                #'Filer Image'
            ],
        ],
        'extraPlugins': ','.join([
            'image2',
            #'filerimage'
        ]),
    }
}


try:
    LOCAL_SETTINGS
except NameError:
    try:
        from local_settings import *
    except ImportError:
        pass
