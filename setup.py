from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

long_description = 'test application'


setup(
    name='test_app',

    version='0.2.0',
    description = 'test application',
    long_description=long_description,
    # url=
    packages=['test_app'],

    author='M.Ovsiannikov',
    author_email='ardling@gmail.com',

    license='GPLv3',

    entry_points={
        'console_scripts': [
            'test_app=test_app.app:main',
        ],
    },

    install_requires=[
        'fastapi',
        'gunicorn',
        'PyYAML',
        'uvicorn',
    ],
    extras_require={
        "testing": [
            "pytest>=5.0.0",
            "pytest-httpserver",
            "pytest-cov"
        ]
    }
)
