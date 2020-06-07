# generate dist
# python3 setup.py sdist bdist_wheel
# python3 -m twine  upload dist/*

# testing commands
# python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# python3 -m pip install -i https://test.pypi.org/simple/ scrapeGG==0.0.1 --user

import setuptools

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    # details
    name='scrapeGG',
    version='0.0.5',
    description='Pulling League of Legends profile and match data from op.gg website.',
    long_description=long_description,
    url='https://github.com/emily-yu/scrape.gg',

    # author
    author='Emily Yu',
    author_email='eyudeveloper@gmail.com',

    # Choose your license
    license='MIT',

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    keywords = 'league development selenium webscraper',

    packages = setuptools.find_packages('src'),
    package_dir = {'': 'src'},
    python_requires = '>=3',
    py_modules = ["scrapeGG", "match_detail", "profile_detail", "utility"],
    include_package_data = True,
    zip_safe = False,
)