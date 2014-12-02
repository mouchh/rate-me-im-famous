try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Rate your iTunes tracks depending on their popularity on the internet',
    'author': 'Cyril Mouchel',
    'url': 'https://github.com/mouchh/rate-me-im-famous',
    'download_url': 'https://github.com/mouchh/rate-me-im-famous/archive/master.zip',
    'author_email': 'mouchel.cyril@gmail.com',
    'version': '1.0',
    'install_requires': [],
    'packages': [],
    'scripts': [],
    'name': 'rate-me-im-famous',
    'platforms': ['mac']
}

setup(**config)
