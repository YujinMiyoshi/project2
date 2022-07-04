from todoproject.settings import BASE_DIR, DEBUG


SECRET_KEY = '%cla9i)!2u)4(1)hev!d67_lve!*q-9xt!r552im7f-cjh+m2j' 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True