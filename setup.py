import setuptools

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    # details
    name='scrape.gg',
    version='1.0.0',
    description='league of legends data from op.gg',
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

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    python_requires = '>=3',
    py_modules = ["scrape.gg"],
    include_package_data = True,
    zip_safe = False,

    install_requires=['requests', 'google'],
)