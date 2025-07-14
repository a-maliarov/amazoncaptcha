# -*- coding: utf-8 -*-

import setuptools
import os

# --------------------------------------------------------------------------------------------------------------

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'amazoncaptcha', '__version__.py'), 'r', encoding='utf-8') as f:
    file_data = [i.replace('\n', '').replace('\'', '').split(' = ') for i in f.readlines()]
    about = {k: v for k, v in file_data}


def readme(logo_end_line=14):
    """Extracts the logo from README file before pushing to PyPi."""

    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = ''.join(fh.readlines()[logo_end_line:])

    return long_description

license = "MIT"

classifiers = [
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Operating System :: OS Independent",
    "Development Status :: 5 - Production/Stable",
    "Natural Language :: English",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: Information Technology",
]

python_requires = ">=3.9"

requires = [
    "pillow >= 9.0.1",
    "requests >= 2.27.1"
]

# --------------------------------------------------------------------------------------------------------------

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    packages=['amazoncaptcha'],
    py_modules=['devtools', 'exceptions', 'solver', 'utils'],
    include_package_data=True,
    package_data={'': ['*.json'], 'amazoncaptcha': ['training_data/*.*']},
    classifiers=classifiers,
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=requires,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    project_urls={
        'Documentation': 'https://amazoncaptcha.readthedocs.io/en/latest/',
        'Source': about['__url__'],
    },
)

# --------------------------------------------------------------------------------------------------------------
