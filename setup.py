try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
}

setup(
    name = 'Panoptes Export Downloader',
    description = 'Panoptes Export library',
    author = 'Marten Veldthuis',
    url = 'https://github.com/zooniverse/panoptes-export-reader',
    entry_points = {
        'console_scripts': ['panoptes-expand=panoptes.cli:expand']
    }
)
