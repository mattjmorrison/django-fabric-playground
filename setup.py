
from setuptools import setup

setup(
    name="django-fabric-playground",
    version="0.1",
    description="Django app using Fabric and buildout",
    author="Matthew J. Morrison",

    package_dir={'': 'src'},
    install_requires = (
        'django',
        'django-debug-toolbar',
        'fabric',
    ),
)
