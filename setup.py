try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Panoptes Export library',
    'author': 'Marten Veldthuis',
    'url': 'https://github.com/zooniverse/panoptes-export-reader',
    'name': 'Panoptes Export Downloader'
}

setup(**config)