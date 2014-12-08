try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Rate your iTunes tracks depending on their popularity on the internet',
    'keywords': 'itunes rate song track auto',
    'author': 'Cyril Mouchel',
    'url': 'https://github.com/mouchh/rate-me-im-famous',
    'download_url': 'https://github.com/mouchh/rate-me-im-famous/archive/master.zip',
    'author_email': 'mouchel.cyril@gmail.com',
    'version': '1.0',
    'packages': ['rate-me-im-famous'],
    'name': 'rate-me-im-famous',
    'platforms': ['macosx'],
    'install_requires': ['selenium']
}

setup(**config)
