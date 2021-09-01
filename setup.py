"""setup file for the project."""
# code gratefully take from https://github.com/navdeep-G/setup.py

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'run'
DESCRIPTION = \
    'A package to run experiments.'

URL_GITHUB = "https://github.com/thobl/run"
URL_ISSUES = "https://github.com/thobl/run/issues"
EMAIL = 'authorfirstname.lastname@kit.edu'
AUTHOR = 'Thomas Blaesius'
REQUIRES_PYTHON = '>=3.8'
# What packages are required for this module to be executed?
REQUIRED = ['pathos', 'tqdm', 'filelock']

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's _version.py module as a dictionary.
about = {}
project_slug = "run"

# Where the magic happens:
setup(
    name=NAME,
    version=0.2,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    project_urls={
        "Bug Tracker": URL_ISSUES,
        "Source Code": URL_GITHUB,
        # "Documentation": URL_DOKU,
        # "Homepage": URL,
        # "Related Software": DACS_SOFTWARE},
    },
    py_modules=['run'],
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # 'mycli=mymodule:cli'
    install_requires=REQUIRED,
    include_package_data=True,
    # license='BSD 3-Clause',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)

